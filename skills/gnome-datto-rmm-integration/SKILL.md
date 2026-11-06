---
name: gnome-datto-rmm-integration
description: Integrate Datto RMM API skills and tools for automated endpoint management and monitoring.
triggers: ["datto rmm", "datto rmm api", "endpoint management integration", "datto python tools"]
---

# Datto RMM Integration Skill

## Overview
Provides Python-based tools and procedures to interface with the Datto RMM API for remote monitoring, management, and device auditing.

## Proven Procedure
1. Create a dedicated skill directory (`skills/datto_rmm/`).
2. Implement authentication and REST client handlers in `tools.py` for Datto RMM's regional API endpoints.
3. Document API usage, rate limits, and common payload formats in `SKILL.md`.

## Pitfalls & Troubleshooting
- Ensure proper regional API URL routing (e.g., `https://api.datto.com/rmm/v1/...` vs regional datacenters).
- Handle OAuth2 or API key authentication headers correctly to avoid 401 unauthorized errors.
