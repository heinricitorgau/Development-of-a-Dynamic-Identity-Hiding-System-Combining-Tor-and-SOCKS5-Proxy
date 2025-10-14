# Development of a Dynamic Identity Hiding System Combining Tor and SOCKS5 Proxy

**Short description**  
Implements an automated IP-rotation controller that interfaces with Tor's ControlPort and routes traffic through a SOCKS5 proxy; optionally supports obfs4 bridges for DPI resistance.

---

## Key Techniques
- Tor ControlPort automation to request new circuits (NEWNYM) programmatically.
- Routing and verification of traffic via local SOCKS5 (socks5h://127.0.0.1:9050).
- obfs4 bridge support for environments subject to DPI/censorship.

---

## Prerequisites
- Debian/Kali Linux with Tor installed and ControlPort enabled.
- Python 3 environment with `stem` and `requests[socks]` (or equivalent).
- Local SOCKS5 proxy (Tor service) reachable at 127.0.0.1:9050.

---

## Quick Start (summary — non-executable)
1. Ensure Tor is configured with ControlPort and authentication (cookie or password).  
2. Review `ghost_mode3.py` configuration options (interval, verification endpoint).  
3. Launch the script in the isolated test environment and observe printed status and IP verification outputs.

> The script includes logging and error handling; review tor logs if identity changes fail.

---

## Safety & Ethics
- Use for privacy research and testing only.
- Do not use to perform illegal acts, abuse third-party services, or bypass local laws and regulations.
- Respect terms-of-service of remote endpoints; use test endpoints when possible.

---

## Troubleshooting & Notes
- If using obfs4, confirm `obfs4proxy` installation and valid bridge lines in `torrc`.
- DNS leaks: ensure local resolver does not leak host DNS queries (consider locking `/etc/resolv.conf` in controlled setups).

---

## Artifacts
- `ghost_mode3.py` — controller script.
- `docs/` — test logs, success/failure statistics, obfs4 instructions.
