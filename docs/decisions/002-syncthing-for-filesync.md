---
status: accepted
date: 2026-04-18
---

# Use Syncthing for file synchronisation

## Context and Problem Statement

Downloaded audio files on the Pi need to reach the phone automatically over WiFi, without requiring the user to manually transfer them.

## Considered Options

- Syncthing (open-source P2P sync)
- Custom rsync/SCP script triggered from the Android app
- Nextcloud self-hosted

## Decision Outcome

**Chosen: Syncthing.**

### Reasons

- Zero custom sync code — Pi is send-only, phone is receive-only; Syncthing handles conflict resolution, retries, and partial transfers automatically
- WiFi-only operation is a built-in setting (no accidental mobile data usage)
- No server component to maintain — purely P2P
- Works transparently over Tailscale when off home WiFi

### Consequences

- Syncthing must be installed on both the Pi (Docker container) and the phone (Syncthing-Fork app)
- Initial pairing setup is manual (one-time, via web UI at port 8384)
- Nextcloud would add a full cloud stack for no benefit in a single-user setup
