---
name: kde-python-real-debrid-gui-automation
description: A template and structural pattern for building Python/tkinter GUI applications that interface with the Real-Debrid API for searching, downloading, and streaming media.
triggers: ["create real-debrid gui app", "tkinter real-debrid integration", "python api app for real-debrid", "build media downloader with real-debrid"]
---

# Python Real-Debrid GUI Automation

## Overview
This skill provides a reusable framework for building GUI applications that utilize the Real-Debrid API. It simplifies the setup of the API client, handles secure API key management, manages the asynchronous nature of API requests using `threading` to keep the GUI responsive, and structures the `tkinter` Treeview component for displaying dynamic results.

## Proven Procedure

### 1. Project Dependencies
Ensure the following libraries are installed to handle HTTP requests and GUI layout.
```bash
pip install requests
```

### 2. Core Structure (Template)
Use the following modular approach for new Real-Debrid applications:

*   **`api_client.py`**: A wrapper class for `requests` that handles authentication headers (`Authorization: Bearer <API_KEY>`) and endpoint abstraction (e.g., `/torrents`, `/unrestrict/link`).
*   **`gui_app.py`**: The `tkinter` implementation. 
    *   **Important Pattern**: Always wrap API calls in a separate thread (using `threading.Thread`) so the GUI does not freeze while waiting for network responses.

### 3. Key Implementation Logic
When integrating, follow this pattern for the search-to-download workflow:

```python
import threading
import requests

# Example: API Interaction Pattern
def perform_search(query):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"https://api.real-debrid.com/rest/1.0/torrents/search?query={query}", headers=headers)
    return response.json()

# Example: Threading Pattern
def on_search_button_click():
    query = entry.get()
    # Run in thread to keep GUI responsive
    threading.Thread(target=lambda: update_treeview(perform_search(query))).start()
```

## Pitfalls & Troubleshooting
*   **GUI Blocking**: **Never** call `requests.get()` directly in the main thread (the main loop). The GUI will freeze until the API returns a response. Always use `threading` or `asyncio`.
*   **API Rate Limiting**: Real-Debrid has strict rate limits. Implement a simple delay or retry logic in your API client wrapper if you trigger multiple requests in rapid succession.
*   **API Key Exposure**: Do not hardcode the API key in the main script. Use a `.env` file or an `~/.config/appname/config.json` file, and ensure your GUI provides a settings menu to update this via `tkinter.Entry` widget.
*   **SSL Errors**: If you encounter SSL errors on the local network, ensure the `certifi` package is updated (`pip install --upgrade certifi`).
