---
name: ai-local-voice-pipeline
description: Implements an offline Speech-to-Text (STT) and Text-to-Speech (TTS) pipeline using local lightweight models like Whisper.cpp and Piper.
triggers: ["offline speech to text", "local tts stt pipeline", "whisper.cpp piper voice assistant", "offline voice interaction"]
---

# Local Offline Speech-to-Text and Text-to-Speech Pipeline

## Overview
This skill provides a complete workflow for establishing an offline, privacy-focused voice interaction loop using lightweight local models: Whisper.cpp for Speech-to-Text (STT) and Piper for Text-to-Speech (TTS).

## Proven Procedure
1. **Prerequisites & Dependencies**:
   - Ensure Python 3.8+ is installed with sounddevice, numpy, and scipy for audio handling.
   - Install `whisper.cpp` and download a lightweight model (e.g., `tiny.en` or `base.en`).
   - Install `piper-tts` and download a compatible voice model (e.g., `en_US-lessac-medium`).

2. **Pipeline Implementation (`voice_pipeline.py`)**:
   ```python
   import subprocess
   import tempfile
   import os
   import sounddevice as sd
   import numpy as np
   import scipy.io.wavfile as wav

   class LocalVoicePipeline:
       def __init__(self, whisper_path="/usr/local/bin/whisper", model_path="/path/to/ggml-base.en.bin", piper_path="/usr/local/bin/piper", piper_model="/path/to/model.onnx"):
           self.whisper_path = whisper_path
           self.model_path = model_path
           self.piper_path = piper_path
           self.piper_model = piper_model

       def listen_and_transcribe(self, duration=5, samplerate=16000):
           print("Listening...")
           audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
           sd.wait()
           
           with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
               wav.write(f.name, samplerate, audio)
               temp_wav = f.name

           try:
               cmd = [self.whisper_path, "-m", self.model_path, "-f", temp_wav, "-nt"]
               result = subprocess.run(cmd, capture_output=True, text=True, check=True)
               transcript = result.stdout.strip()
               return transcript
           finally:
               os.remove(temp_wav)

       def speak(self, text):
           cmd = [self.piper_path, "--model", self.piper_model, "--output_file", "-"]
           process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
           stdout, _ = process.communicate(input=text.encode('utf-8'))
           
           with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
               f.write(stdout)
               temp_wav = f.name

           try:
               data, fs = sf.read(temp_wav) # Or use scipy/sounddevice to play
               sd.play(data, fs)
               sd.wait()
           finally:
               os.remove(temp_wav)
   ```

## Pitfalls & Troubleshooting
- **Audio Device Errors**: Ensure `sounddevice` has access to input/output devices (`alsa` or `pulseaudio`/`pipewire` backends configured).
- **Model Paths**: Verify that absolute paths to Whisper and Piper binaries and `.bin`/`.onnx` model files are correct.
