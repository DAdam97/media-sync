---
status: accepted
date: 2026-04-18
---

# Use Tailscale for remote access to the Pi

## Context and Problem Statement

The Android app must reach the Pi's API from any network (home WiFi, other WiFi, mobile data) using a stable address. The Pi is behind a home router with a dynamic public IP and no static DNS.

## Considered Options

- Tailscale (WireGuard-based mesh VPN)
- Dynamic DNS (DDNS) + port forwarding
- Cloudflare Tunnel

## Decision Outcome

**Chosen: Tailscale.**

### Reasons

- Pi gets a fixed Tailscale IP that never changes — the Android app hardcodes this address
- No port forwarding required — eliminates exposure of the Pi directly to the internet
- Works transparently on any network without any app-side configuration changes
- Free tier covers single-user use; Syncthing traffic also routes over it when off home WiFi
- Installed as a system service on the Pi (not in Docker) — survives container restarts

### Consequences

- Both the Pi and the phone must have Tailscale installed and be logged into the same account
- DDNS + port forwarding would work but exposes port 8000 publicly; Tailscale avoids this risk
