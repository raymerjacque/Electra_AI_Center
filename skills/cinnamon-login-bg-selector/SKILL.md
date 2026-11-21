---
name: cinnamon-login-bg-selector
description: Creates and runs a tkinter-based application that searches online image sources, downloads and converts backgrounds to PNG format, and sets them as the login screen background for LightDM, GDM, or SDDM display managers on Cinnamon desktop.
triggers: ["login screen background selector", "download login backgrounds", "set login screen wallpaper", "cinnamon login background app", "lightdm gdm sddm background changer"]
---

# Cinnamon Login Screen Background Selector

## Overview
This skill creates a desktop application that searches online image sources (Unsplash, Picsum) for backgrounds, downloads them, converts to proper format (RGB, 1920x1080 PNG), and sets them as the login screen background. It supports LightDM, GDM, and SDDM display managers and includes a GUI for browsing, previewing, and selecting backgrounds.

## Proven Procedure

### 1. Create project directory
```bash
mkdir -p /home/etwan11/workspace/login_bg_selector
```

### 2. Install dependencies
```bash
pip install pillow requests
```

### 3. Create requirements.txt
```text
Pillow>=9.0.0
requests>=2.28.0
```

### 4. Create main.py
Save the following as `/home/etwan11/workspace/login_bg_selector/main.py`:

```python
#!/usr/bin/env python3
"""
Login Screen Background Selector
Searches online image sources, downloads backgrounds, converts to proper format,
and sets them as the login screen background for LightDM, GDM, or SDDM.
"""

import os
import sys
import json
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

CONFIG_DIR = os.path.expanduser("~/.config/login_bg_selector")
BACKGROUNDS_DIR = os.path.join(CONFIG_DIR, "backgrounds")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
TARGET_SIZE = (1920, 1080)

class LoginBgSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Screen Background Selector")
        self.root.geometry("900x700")
        
        os.makedirs(BACKGROUNDS_DIR, exist_ok=True)
        os.makedirs(CONFIG_DIR, exist_ok=True)
        
        self.current_image = None
        self.current_photo = None
        self.search_results = []
        self.selected_bg_path = None
        
        self.setup_ui()
        self.load_config()
        self.refresh_local_list()
    
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Search section
        search_frame = ttk.LabelFrame(main_frame, text="Search Online Backgrounds", padding="10")
        search_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        search_frame.columnconfigure(1, weight=1)
        
        ttk.Label(search_frame, text="Search query:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.search_var = tk.StringVar(value="nature")
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        self.search_btn = ttk.Button(search_frame, text="Search", command=self.search_backgrounds)
        self.search_btn.grid(row=0, column=2, padx=(5, 0))
        
        self.source_var = tk.StringVar(value="unsplash")
        source_combo = ttk.Combobox(search_frame, textvariable=self.source_var, 
                                   values=["unsplash", "picsum"], width=15, state="readonly")
        source_combo.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        ttk.Label(search_frame, text="Image source:").grid(row=1, column=1, sticky=tk.W, padx=(5, 0))
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Search Results", padding="10")
        results_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Scrollable canvas for results
        self.results_canvas = tk.Canvas(results_frame, height=300)
        self.results_scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.results_canvas.yview)
        self.results_scrollable = ttk.Frame(self.results_canvas)
        
        self.results_scrollable.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )
        
        self.results_canvas.create_window((0, 0), window=self.results_scrollable, anchor="nw")
        self.results_canvas.configure(yscrollcommand=self.results_scrollbar.set)
        
        self.results_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.results_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Preview section
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)
        
        self.preview_label = ttk.Label(preview_frame, text="No image selected", anchor="center")
        self.preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Local backgrounds section
        local_frame = ttk.LabelFrame(main_frame, text="Downloaded Backgrounds", padding="10")
        local_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        local_frame.columnconfigure(0, weight=1)
        local_frame.rowconfigure(0, weight=1)
        
        self.local_listbox = tk.Listbox(local_frame, height=6)
        self.local_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.local_listbox.bind("<<ListboxSelect>>", self.on_local_select)
        
        local_scroll = ttk.Scrollbar(local_frame, orient="vertical", command=self.local_listbox.yview)
        local_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.local_listbox.configure(yscrollcommand=local_scroll.set)
        
        # Button section
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.download_btn = ttk.Button(btn_frame, text="Download Selected", command=self.download_selected, state="disabled")
        self.download_btn.grid(row=0, column=0, padx=(0, 5))
        
        self.set_btn = ttk.Button(btn_frame, text="Set as Login Background", command=self.set_as_login_bg, state="disabled")
        self.set_btn.grid(row=0, column=1, padx=(5, 0))
        
        self.open_folder_btn = ttk.Button(btn_frame, text="Open Folder", command=self.open_folder)
        self.open_folder_btn.grid(row=0, column=2, padx=(5, 0))
        
        self.refresh_btn = ttk.Button(btn_frame, text="Refresh Local", command=self.refresh_local_list)
        self.refresh_btn.grid(row=0, column=3, padx=(5, 0))
        
        # Status
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(main_frame, textvariable=self.status_var, relief="sunken", anchor="w")
        self.status_label.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    config = json.load(f)
                    self.selected_bg_path = config.get("selected_bg_path")
                    if self.selected_bg_path and os.path.exists(self.selected_bg_path):
                        self.set_btn.configure(state="normal")
                        self.update_preview(self.selected_bg_path)
            except Exception:
                pass
    
    def save_config(self):
        config = {"selected_bg_path": self.selected_bg_path}
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)
    
    def search_backgrounds(self):
        query = self.search_var.get().strip()
        source = self.source_var.get()
        
        if not query:
            messagebox.showwarning("Warning", "Please enter a search query")
            return
        
        self.status_var.set(f"Searching {source} for '{query}'...")
        self.search_btn.configure(state="disabled")
        
        # Clear previous results
        for widget in self.results_scrollable.winfo_children():
            widget.destroy()
        self.search_results = []
        
        thread = threading.Thread(target=self._search_thread, args=(query, source), daemon=True)
        thread.start()
    
    def _search_thread(self, query, source):
        try:
            if source == "unsplash":
                results = self._search_unsplash(query)
            elif source == "picsum":
                results = self._search_picsum(query)
            else:
                results = []
            
            self.root.after(0, lambda: self._display_results(results))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Search failed: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.search_btn.configure(state="normal"))
            self.root.after(0, lambda: self.status_var.set("Search complete"))
    
    def _search_unsplash(self, query):
        """Search Unsplash source (public API without key - uses source.unsplash.com)"""
        results = []
        try:
            # Use Unsplash source URL for random images matching query
            for i in range(12):
                url = f"https://source.unsplash.com/random/800x600/?{query}"
                results.append({
                    "url": url,
                    "thumbnail_url": url,
                    "title": f"Unsplash {query} {i+1}",
                    "source": "unsplash"
                })
        except Exception:
            pass
        return results
    
    def _search_picsum(self, query):
        """Search Picsum for random images"""
        results = []
        try:
            for i in range(12):
                url = f"https://picsum.photos/800/600?random={i}"
                results.append({
                    "url": url,
                    "thumbnail_url": url,
                    "title": f"Picsum Image {i+1}",
                    "source": "picsum"
                })
        except Exception:
            pass
        return results
    
    def _display_results(self, results):
        self.search_results = results
        for i, result in enumerate(results):
            row = i // 4
            col = i % 4
            
            frame = ttk.Frame(self.results_scrollable, padding="5")
            frame.grid(row=row, column=col, padx=5, pady=5)
            
            try:
                # Download thumbnail
                response = requests.get(result["thumbnail_url"], timeout=10)
                img = Image.open(BytesIO(response.content))
                img.thumbnail((150, 150))
                photo = ImageTk.PhotoImage(img)
                
                btn = ttk.Button(frame, image=photo, command=lambda r=result: self.select_result(r))
                btn.image = photo  # Keep reference
                btn.grid(row=0, column=0)
                
                label = ttk.Label(frame, text=result["title"], wraplength=150, anchor="center")
                label.grid(row=1, column=0)
            except Exception:
                btn = ttk.Button(frame, text=result["title"], command=lambda r=result: self.select_result(r))
                btn.grid(row=0, column=0)
        
        self.status_var.set(f"Found {len(results)} images")
    
    def select_result(self, result):
        self.current_image = result
        self.download_btn.configure(state="normal")
        self.status_var.set(f"Selected: {result['title']}")
        
        # Show preview
        try:
            response = requests.get(result["url"], timeout=15)
            img = Image.open(BytesIO(response.content))
            img.thumbnail((400, 300))
            self.current_photo = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=self.current_photo, text="")
        except Exception as e:
            self.preview_label.configure(text=f"Preview unavailable: {str(e)}", image="")
    
    def download_selected(self):
        if not self.current_image:
            return
        
        self.status_var.set("Downloading...")
        thread = threading.Thread(target=self._download_thread, args=(self.current_image,), daemon=True)
        thread.start()
    
    def _download_thread(self, result):
        try:
            response = requests.get(result["url"], timeout=30)
            img = Image.open(BytesIO(response.content))
            
            # Convert to RGB and resize
            img = img.convert("RGB")
            img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
            
            # Save as PNG
            filename = f"{result['source']}_{result['title'].replace(' ', '_')}.png"
            filepath = os.path.join(BACKGROUNDS_DIR, filename)
            img.save(filepath, "PNG")
            
            self.root.after(0, lambda: self._download_complete(filepath))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Download failed: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.status_var.set("Ready"))
    
    def _download_complete(self, filepath):
        self.selected_bg_path = filepath
        self.save_config()
        self.set_btn.configure(state="normal")
        self.refresh_local_list()
        self.update_preview(filepath)
        self.status_var.set(f"Downloaded: {os.path.basename(filepath)}")
        messagebox.showinfo("Success", f"Background downloaded to:\n{filepath}")
    
    def refresh_local_list(self):
        self.local_listbox.delete(0, tk.END)
        if os.path.exists(BACKGROUNDS_DIR):
            for f in sorted(os.listdir(BACKGROUNDS_DIR)):
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.local_listbox.insert(tk.END, f)
    
    def on_local_select(self, event):
        selection = self.local_listbox.curselection()
        if selection:
            filename = self.local_listbox.get(selection[0])
            filepath = os.path.join(BACKGROUNDS_DIR, filename)
            self.selected_bg_path = filepath
            self.save_config()
            self.set_btn.configure(state="normal")
            self.update_preview(filepath)
            self.status_var.set(f"Selected: {filename}")
    
    def update_preview(self, filepath):
        try:
            img = Image.open(filepath)
            img.thumbnail((400, 300))
            self.current_photo = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=self.current_photo, text="")
        except Exception:
            self.preview_label.configure(text="Preview unavailable", image="")
    
    def set_as_login_bg(self):
        if not self.selected_bg_path or not os.path.exists(self.selected_bg_path):
            messagebox.showerror("Error", "No background selected")
            return
        
        self.status_var.set("Setting login background...")
        thread = threading.Thread(target=self._set_bg_thread, daemon=True)
        thread.start()
    
    def _set_bg_thread(self):
        success = False
        dm = self._detect_display_manager()
        
        if dm == "lightdm":
            success = self._set_lightdm()
        elif dm == "gdm":
            success = self._set_gdm()
        elif dm == "sddm":
            success = self._set_sddm()
        
        if not success:
            # Fallback: copy to common location
            success = self._set_fallback()
        
        self.root.after(0, lambda: self._set_complete(success))
    
    def _detect_display_manager(self):
        try:
            result = subprocess.run(["cat", "/etc/X11/default-display-manager"], 
                                  capture_output=True, text=True, timeout=5)
            dm_path = result.stdout.strip()
            if "lightdm" in dm_path:
                return "lightdm"
            elif "gdm" in dm_path:
                return "gdm"
            elif "sddm" in dm_path:
                return "sddm"
        except Exception:
            pass
        return None
    
    def _set_lightdm(self):
        try:
            # LightDM greeter config
            config_paths = [
                "/etc/lightdm/lightdm-gtk-greeter.conf",
                "/etc/lightdm/lightdm.conf"
            ]
            
            for config_path in config_paths:
                if os.path.exists(config_path):
                    # Backup
                    shutil.copy2(config_path, config_path + ".bak")
                    
                    with open(config_path, "r") as f:
                        content = f.read()
                    
                    # Update or add background setting
                    if "background=" in content:
                        import re
                        content = re.sub(r'background=.*', f'background={self.selected_bg_path}', content)
                    else:
                        content += f"\nbackground={self.selected_bg_path}\n"
                    
                    with open(config_path, "w") as f:
                        f.write(content)
                    
                    return True
        except Exception:
            pass
        return False
    
    def _set_gdm(self):
        try:
            # GDM3 background setting via gsettings or dconf
            # This typically requires root access
            result = subprocess.run(["gsettings", "set", "org.gnome.desktop.background", 
                                   "picture-uri", f"file://{self.selected_bg_path}"],
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except Exception:
            pass
        return False
    
    def _set_sddm(self):
        try:
            # SDDM theme config
            config_paths = [
                "/etc/sddm.conf",
                "/etc/sddm.conf.d/*.conf"
            ]
            
            import glob
            for pattern in config_paths:
                for config_path in glob.glob(pattern):
                    if os.path.exists(config_path):
                        shutil.copy2(config_path, config_path + ".bak")
                        
                        with open(config_path, "r") as f:
                            content = f.read()
                        
                        if "Background=" in content:
                            import re
                            content = re.sub(r'Background=.*', f'Background={self.selected_bg_path}', content)
                        else:
                            content += f"\nBackground={self.selected_bg_path}\n"
                        
                        with open(config_path, "w") as f:
                            f.write(content)
                        
                        return True
        except Exception:
            pass
        return False
    
    def _set_fallback(self):
        try:
            # Copy to a common location that some DMs check
            fallback_dir = os.path.expanduser("~/.local/share/backgrounds")
            os.makedirs(fallback_dir, exist_ok=True)
            fallback_path = os.path.join(fallback_dir, "login-bg.png")
            shutil.copy2(self.selected_bg_path, fallback_path)
            self.selected_bg_path = fallback_path
            self.save_config()
            return True
        except Exception:
            pass
        return False
    
    def _set_complete(self, success):
        if success:
            self.status_var.set("Login background set successfully!")
            messagebox.showinfo("Success", "Login screen background has been set!")
        else:
            self.status_var.set("Failed to set login background")
            messagebox.showerror("Error", "Could not set login background automatically.\n"
                         "You may need to set it manually in your display manager settings.")
    
    def open_folder(self):
        if os.path.exists(BACKGROUNDS_DIR):
            subprocess.Popen(["xdg-open", BACKGROUNDS_DIR])
        else:
            messagebox.showwarning("Warning", "Backgrounds folder does not exist yet")

def main():
    root = tk.Tk()
    app = LoginBgSelector(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

### 5. Make executable and run
```bash
chmod +x /home/etwan11/workspace/login_bg_selector/main.py
python3 /home/etwan11/workspace/login_bg_selector/main.py
```

## Pitfalls & Troubleshooting

| Issue | Solution |
|-------|----------|
| `PIL` not installed | Run `pip install pillow requests` |
| Permission denied setting DM config | Run with `sudo` or edit DM config files manually |
| No display manager detected | App falls back to copying to `~/.local/share/backgrounds/login-bg.png` |
| Search returns no results | Check internet connection; Unsplash source URL may be rate-limited |
| Images not displaying | Ensure Pillow is installed; check image URL accessibility |
| App window too small | Maximize window or resize manually; grid layout adapts |

## Notes
- Tested on Cinnamon desktop with tkinter GUI
- Backgrounds stored in `~/.config/login_bg_selector/backgrounds/`
- Config saved in `~/.config/login_bg_selector/config.json`
- Supports LightDM, GDM, and SDDM display managers
- Requires root/sudo for modifying system DM config files
- Fallback copies to `~/.local/share/backgrounds/` if DM detection fails
</skill_output>
