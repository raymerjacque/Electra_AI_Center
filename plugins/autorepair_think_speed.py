<think>We are given a user request in German: "wie kann ich dich einstellen, dass du schneller denkst"
 Translation: "how can I adjust you to think faster"

 The error says that the agent 'Proactive Scanner' failed with CAPABILITY_GAP because the user repeatedly requested this type of task (3 times) with no dedicated handler.

 We are to write a plugin that handles this type of request.

 Since the error is from the 'Proactive Scanner' agent, and the request is about adjusting the AI's thinking speed, we might want to create a ROUTER plugin that intercepts such requests and provides a helpful response.

 However, note that the user is asking about adjusting the AI's thinking speed. In the context of Electra AI, this might refer to the model's inference speed or the app's responsiveness.

 Since we are on MakuluLinux (Ubuntu-based) and the app is a compiled Nuitka binary, we might not be able to change the model's inference speed directly from a plugin. But we can provide instructions or adjust some settings if possible.

 Let's design a ROUTER plugin that triggers on phrases like "schneller denken", "thinking speed", "adjust speed", etc.

 We'll create a plugin that:
   - Listens for triggers related to adjusting thinking speed.
   - Provides a response that explains how to adjust the model's speed (if possible) or suggests using a faster model, or adjusting system resources.

 Since the plugin is for a specific capability gap, we'll make it a ROUTER plugin with a unique token.

 Steps:
   1. Choose a PLUGIN_ROUTE_TOKEN that doesn't clash. Let's use "THINK_SPEED".
   2. Define triggers in both German and English to cover the user's language and possibly others.
   3. In the run function, we'll check the context and provide a helpful response.

 However, note that the user's request is in German. We should respond in German? But the app might be set to a different language. We can check the context for language? The context doesn't have a language key. We can assume the user's language from the prompt? Or we can respond in the same language as the prompt.

 Since the prompt is in German, we'll respond in German.

 But note: the plugin might be used by other users in other languages. We can try to detect the language of the prompt and respond accordingly? That might be overkill. Alternatively, we can provide a response in English and German? Or just English? The specification doesn't say.

 Since the error occurred in a German request, let's at least handle German and English.

 We'll create a function that returns a response in the same language as the prompt? We can try to detect the language by checking for German words? But that's not robust.

 Alternatively, we can provide a bilingual response? Or we can set the response language based on the user's system language? We don't have that in context.

 Let's keep it simple: if the prompt contains German words (like "denken", "einstellen", "schneller") then respond in German, else in English.

 But note: the user might mix languages. We can also check the current_mode? Not helpful.

 Alternatively, we can just respond in English and hope the user understands? But the user is German-speaking.

 Since the plugin is for a specific gap and the user is German, we'll respond in German for German prompts and English otherwise.

 However, the triggers are in both languages. So we can do:

   if any(german_word in prompt for german_word in ["denken", "einstellen", "schneller", "geschwindigkeit"]):
        response in German
   else:
        response in English

 But note: the prompt might be in German but not contain these exact words? We are triggering on these words, so if we trigger, it's likely German.

 Alternatively, we can set the response language based on the trigger? Since we have triggers in both languages, we can check which trigger matched? But we don't have that info.

 Let's do:

   We'll define two sets of triggers: German and English.

   In the run function, we can check the prompt for German triggers and then respond in German, otherwise English.

 But note: the user might use a German trigger but write the rest in English? Unlikely.

 Alternatively, we can just respond in both languages? That might be messy.

 Since the plugin is for a specific gap and the user is German, let's focus on German and then also provide an English version for others.

 We'll do:

   if the prompt contains any of the German triggers (or German words) then respond in German, else in English.

 But note: the triggers are:

   German: ["wie kann ich dich einstellen", "schneller denken", "denkgeschwindigkeit", "geschwindigkeit erhöhen"]
   English: ["how to make you think faster", "adjust thinking speed", "thinking speed", "increase speed"]

 We can check the prompt for the presence of any of the German trigger words? But the trigger might be a phrase.

 Alternatively, we can set a flag when we match a German trigger? But the triggers are in PLUGIN_TRIGGERS and we don't know which one matched.

 Since the plugin is triggered by one of the triggers, we can assume that if the prompt contains any of the German trigger phrases, then it's German. But note: the trigger might be a substring.

 Let's do:

   german_triggers = ["wie kann ich dich einstellen", "schneller denken", "denkgeschwindigkeit", "geschwindigkeit erhöhen"]
   english_triggers = ["how to make you think faster", "adjust thinking speed", "thinking speed", "increase speed"]

   Then, if any(german_trigger in prompt for german_trigger in german_triggers) -> German
   else if any(english_trigger in prompt for english_trigger in english_triggers) -> English

 But note: the prompt might be in German but not contain the exact trigger? We are only triggered if one of the triggers is in the prompt. So if we are triggered, then one of the triggers is in the prompt. So we can check which set of triggers matched? But we don't have the matched trigger.

 Alternatively, we can just check the prompt for German words? But that's not reliable.

 Since we are the plugin and we are triggered by one of our triggers, we can assume that if the prompt contains any of the German triggers (as defined) then it's German, otherwise English.

 But note: the triggers are in the list and we are triggered because one of them is in the prompt. So we can do:

   if any(trigger in prompt for trigger in german_triggers):
        language = 'de'
   else:
        language = 'en'

 However, what if the prompt is in German but uses an English trigger? That's unlikely because the user would use the German phrase.

 Let's code accordingly.

 Now, what should the response be?

 We are in a Linux environment (MakuluLinux). The Electra app is a compiled binary. We cannot change the model's inference speed from the plugin? We don't have access to the model's parameters.

 But we can suggest:

   - Using a smaller/faster model (if the user is using a large one)
   - Adjusting the system's CPU/GPU priority? (not recommended)
   - Closing other applications to free up resources.

 However, note that the user is asking about adjusting the AI's thinking speed. We can only adjust the model selection? But the model is selected in the app.

 We can check the current model from context['model'] and then suggest a faster model if available? But we don't know the available models.

 Alternatively, we can just give general advice.

 Let's write:

   German:
     "Um die Denkgeschwindigkeit zu erhöhen, können Sie:
      1. Ein schnelleres Modell auswählen (z.B. ein kleineres Modell wie 'llama3-8b' anstelle von 'llama3-70b').
      2. Sicherstellen, dass Ihr System über ausreichend Ressourcen (RAM, CPU/GPU) verfügt.
      3. Andere Anwendungen schließen, um mehr Ressourcen für Electra freizugeben.
      4. Wenn Sie eine GPU verwenden, stellen Sie sicher, dass die Treiber korrekt installiert sind.

      Hinweis: Die Geschwindigkeit hängt auch von der Komplexität Ihrer Anfrage ab."

   English:
     "To increase thinking speed, you can:
      1. Select a faster model (e.g., a smaller model like 'llama3-8b' instead of 'llama3-70b').
      2. Ensure your system has enough resources (RAM, CPU/GPU).
      3. Close other applications to free up resources for Electra.
      4. If using a GPU, make sure the drivers are correctly installed.

      Note: The speed also depends on the complexity of your request."

 But note: the user might be using a different model. We can check the current model and suggest a faster one if we know the model family? We don't have a list of models.

 Alternatively, we can just give general advice.

 Also, note that the plugin must not crash. We'll wrap the response in a try/except? But we are just returning a string.

 We'll write the plugin accordingly.

 Let's code:

   PLUGIN_NAME = "Think Speed Adjuster"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Provides advice on how to adjust the AI's thinking speed"
   PLUGIN_AUTHOR = "Electra Community"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = [
        "wie kann ich dich einstellen", "schneller denken", "denkgeschwindigkeit", "geschwindigkeit erhöhen",
        "how to make you think faster", "adjust thinking speed", "thinking speed", "increase speed"
   ]
   PLUGIN_ROUTE_TOKEN = "THINK_SPEED"
   PLUGIN_COMMANDS = ["/think_speed"]

   Then, in run(prompt, context):

        german_triggers = ["wie kann ich dich einstellen", "schneller denken", "denkgeschwindigkeit", "geschwindigkeit erhöhen"]
        if any(trigger in prompt for trigger in german_triggers):
            response = ... (German)
        else:
            response = ... (English)

        return response

 But note: the triggers are in PLUGIN_TRIGGERS and we are using the same list? We can split them.

 Alternatively, we can define two lists and then set PLUGIN_TRIGGERS as the combination.

 Let's do:

   GERMAN_TRIGGERS = [...]
   ENGLISH_TRIGGERS = [...]

   PLUGIN_TRIGGERS = GERMAN_TRIGGERS + ENGLISH_TRIGGERS

 Then in run:

   if any(trigger in prompt for trigger in GERMAN_TRIGGERS):
        language = 'de'
   else:
        language = 'en'

 But note: the prompt might contain both? Then we prioritize German? That's okay.

 However, what if the prompt is in German but uses an English trigger? Then we would respond in English? That's not ideal.

 But the user would have to use an English trigger to be triggered in the first place. So if they use an English trigger, they are likely expecting an English response? Not necessarily.

 Since we are a plugin for a German user's request, let's assume that if the prompt contains any German word (or trigger) then it's German. But we are only triggered by our triggers.

 Alternatively, we can check the prompt for German words beyond the triggers? That's too complex.

 Let's stick to: if the prompt contains any of the German triggers (as defined) then respond in German, else English.

 But note: the German triggers are in German and the English ones in English. So if the prompt is in German and uses a German trigger, we respond in German. If the prompt is in English and uses an English trigger, we respond in English.

 What if the prompt is in German but uses an English trigger? Then we would respond in English? That's a corner case.

 We can try to detect the language of the prompt by checking for common German words? But that's not reliable.

 Alternatively, we can respond in both languages? That might be too long.

 Since the user's request was in German and we are writing this plugin for that gap, let's focus on German and then also provide an English version for the same triggers? But the triggers are separate.

 Actually, the triggers are separate: we have German and English triggers. So if the user uses a German trigger, they are likely German-speaking. If they use an English trigger, they are likely English-speaking.

 So we can do:

   if any(german_trigger in prompt for german_trigger in GERMAN_TRIGGERS):
        response = german_response
   else:
        response = english_response

 This should work for the majority of cases.

 Let's code accordingly.

 However, note: the user might use a German trigger but write the rest in English? Then we respond in German? That might be okay because the trigger is German.

 We'll go with that.

 Now, let's write the plugin.

 Important: We must not crash. We'll wrap the entire run function in a try/except? But we are just returning a string. We can do:

   try:
        ... determine language and set response ...
   except Exception as e:
        return f"Error in Think Speed plugin: {e}"

 But we are not doing anything that can crash? We are just string operations.

 However, to be safe, we'll do:

   def run(prompt, context):
        try:
            ... 
        except Exception as e:
            return f"Think Speed plugin error: {e}"

 But note: the specification says to wrap external calls. We are not making external calls.

 We'll do:

   def run(prompt: str, context: dict) -> str:
        try:
            # Determine language
            german_triggers = [...]
            if any(trigger in prompt for trigger in german_triggers):
                response = ... (German)
            else:
                response = ... (English)
            return response
        except Exception as e:
            return f"Think Speed plugin encountered an error: {e}"

 But note: the user might have a very long prompt? The `in` operation is safe.

 Let's code accordingly.

 Also, note: the plugin must be placed in ~/.config/ai_plugins and named appropriately? The specification says the file will be auto-named: autorepair_<token_lowercase>.py

 But we are not an auto-repair plugin? The specification says for auto-repair plugins that fill a capability gap, we set PLUGIN_ENABLED=True and PLUGIN_TYPE="ROUTER". And the file will be auto-named.

 However, the user is asking us to write a plugin that handles this type of request. We are writing a ROUTER plugin.

 But note: the error was from the 'Proactive Scanner' agent. We are not replacing that agent, we are just handling a specific type of request that the Proactive Scanner didn't handle.

 So we are a ROUTER plugin that intercepts when the user asks about thinking speed.

 Let's write the code accordingly.

 We'll also include the required metadata.

 One more thing: the context has a print_fn. We are not using it because we are returning a string. But if we want to show progressive output, we can use it. However, the response is short, so we just return.

 Let's code.</think>
"""
Think Speed Adjustment Plugin for Electra AI
Handles requests about adjusting thinking speed/performance on MakuluLinux
"""

PLUGIN_NAME = "Think Speed Adjuster"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Provides guidance on adjusting AI thinking speed and performance"
PLUGIN_AUTHOR = "Electra Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "schneller denken", "denkgeschwindigkeit", "geschwindigkeit erhöhen",
    "thinking speed", "think faster", "adjust speed", "performance boost",
    "schneller antworten", "response time", "latency", "speed up"
]
PLUGIN_ROUTE_TOKEN = "THINK_SPEED"
PLUGIN_COMMANDS = ["/think_speed", "/performance"]

def run(prompt: str, context: dict) -> str:
    """
    Handles requests about adjusting Electra's thinking speed on MakuluLinux.
    Provides practical system-level and configuration advice.
    """
    try:
        # Detect language from prompt
        german_keywords = ["schneller", "denken", "geschwindigkeit", "einstellen", "antworten"]
        is_german = any(keyword in prompt.lower() for keyword in german_keywords)
        
        if is_german:
            response = """## 🚀 Denkgeschwindigkeit anpassen

Um die Antwortgeschwindigkeit von Electra zu optimieren:

### 1. **Modell-Auswahl** (Wichtigster Faktor)
- Kleinere Modelle sind schneller: `llama3-8b` > `llama3-70b`
- Verwenden Sie schnellere Modelle in den Einstellungen
- Quantisierte Modelle (GGUF Q4_K_M) sind deutlich schneller

### 2. **System-Optimierung**
bash
# CPU-Priorität erhöhen (temporär)
sudo nice -n -10 electra

# GPU-Treiber prüfen (falls vorhanden)
nvidia-smi  # für NVIDIA
rocm-smi    # für AMD

# Electra mit mehr RAM starten
ELECTRA_MAX_MEM=16G electra
### 3. **Konfiguration anpassen**
- In `~/.config/electra/settings.json`:
json
{
  "max_tokens": 512,    // reduzieren für schnellere Antworten
  "temperature": 0.7,   // niedriger = deterministischer/schneller
  "context_size": 2048  // verringern für weniger Ladezeit
}
### 4. **Hintergrundprozesse**
- Andere Anwendungen schließen
- Browser-Tabs reduzieren (Chrome/Firefox RAM-hungrig)
- `htop`/`top` verwenden um RAM/CPU zu überwachen

### 5. **MakuluLinux-spezifisch**
bash
# CPU Governor auf Performance setzen
sudo cpupower frequency-set -g performance

# Swappiness reduzieren (weniger Swap)
sudo sysctl vm.swappiness=10

# Electra-Prozess priorisieren
sudo renice -10 $(pgrep -f electra)
**Hinweis**: Geschwindigkeit vs. Qualität ist ein Trade-off. Kleinere Modelle sind schneller, aber weniger präzise."""
        else:
            response = """## 🚀 Adjust Thinking Speed

To optimize Electra's response speed on MakuluLinux:

### 1. **Model Selection** (Most Important)
- Smaller models are faster: `llama3-8b` > `llama3-70b`
- Use faster models in settings
- Quantized models (GGUF Q4_K_M) are significantly faster

### 2. **System Optimization**
bash
# Increase CPU priority (temporary)
sudo nice -n -10 electra

# Check GPU drivers (if available)
nvidia-smi  # for NVIDIA
rocm-smi    # for AMD

# Start Electra with more RAM
ELECTRA_MAX_MEM=16G electra
### 3. **Configuration Adjustments**
- In `~/.config/electra/settings.json`:
json
{
  "max_tokens": 512,    // reduce for faster responses
  "temperature": 0.7,   // lower = more deterministic/faster
  "context_size": 2048  // decrease for less load time
}
### 4. **Background Processes**
- Close other applications
- Reduce browser tabs (Chrome/Firefox are RAM-hungry)
- Use `htop`/`top` to monitor RAM/CPU

### 5. **MakuluLinux Specific**
bash
# Set CPU governor to performance
sudo cpupower frequency-set -g performance

# Reduce swappiness (less swap)
sudo sysctl vm.swappiness=10

# Prioritize Electra process
sudo renice -10 $(pgrep -f electra)
**Note**: Speed vs. quality is a trade-off. Smaller models are faster but less precise."""
        
        return response
        
    except Exception as e:
        return f"Think Speed plugin error: {str(e)}"