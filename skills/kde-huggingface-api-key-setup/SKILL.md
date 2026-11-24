---
name: kde-huggingface-api-key-setup
description: Automates Hugging Face API token setup, persistence in ~/.bashrc, and verification via python huggingface_hub.
triggers: ["test huggingface api key", "setup huggingface token", "huggingface bash script", "hf_token setup"]
---

# Hugging Face API Key Setup and Verification

## Overview
Automates the configuration, persistence, and verification of Hugging Face API keys using a bash script and python verification snippets.

## Proven Procedure
1. Create a bash script (`setup_huggingface.sh`) to prompt for the API token, export it to the current environment, and append it to `~/.bashrc`:
```bash
#!/bin/bash
read -p "Enter your Hugging Face API token: " HF_TOKEN_VAL
export HUGGINGFACE_API_KEY="$HF_TOKEN_VAL"
export HF_TOKEN="$HF_TOKEN_VAL"

# Add to ~/.bashrc if not already present
if ! grep -q "HUGGINGFACE_API_KEY" ~/.bashrc; then
    echo "export HUGGINGFACE_API_KEY=\"$HF_TOKEN_VAL\"" >> ~/.bashrc
    echo "export HF_TOKEN=\"$HF_TOKEN_VAL\"" >> ~/.bashrc
    echo "Added tokens to ~/.bashrc"
fi
source ~/.bashrc
```

2. Test the connection using Python (`huggingface_hub`):
```python
from huggingface_hub import HfApi
import os
api = HfApi()
print(api.whoami(token=os.environ.get('HUGGINGFACE_API_KEY')))
```

## Pitfalls & Troubleshooting
- Ensure `huggingface_hub` python package is installed via `pip install huggingface_hub`.
- Make sure to run `source ~/.bashrc` or restart the terminal session if the environment variable isn't picked up immediately.
