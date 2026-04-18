---
status: accepted
date: 2026-04-18
---

# Use a static API key for authentication

## Context and Problem Statement

The FastAPI backend must be protected so that only the owner's Android app can call it. The system has exactly one user.

## Considered Options

- Static API key (`Authorization: Bearer <key>`)
- JWT (JSON Web Tokens)
- OAuth 2.0

## Decision Outcome

**Chosen: static API key.**

### Reasons

- Single-user app — there are no multiple accounts, sessions, or token refresh flows to manage
- The key is set once as an env var on the Pi and stored in `EncryptedSharedPreferences` on the phone
- Implementation is a single FastAPI dependency function (~5 lines); JWT/OAuth would add libraries and complexity for zero security benefit in this context
- Combined with Tailscale (traffic never hits the public internet), the threat model does not require short-lived tokens

### Consequences

- Key rotation requires updating the env var on Pi and the stored value on the phone manually
- `GET /api/health` is intentionally exempt from auth — used by the app to check Pi reachability
