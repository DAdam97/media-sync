# MediaSync

A personal media sync system that saves mobile data. Submit YouTube / YouTube Music links from your phone → Raspberry Pi 4 downloads and processes the audio → files sync back over WiFi → Poweramp plays them.

## Architecture

```
┌─────────────────┐         REST API          ┌──────────────────────┐
│   Android App   │ ◄──────(Retrofit)────────► │   Raspberry Pi 4     │
│   (Kotlin)      │                            │   (FastAPI backend)  │
│                 │                            │                      │
│ • Link submit   │   ◄── Syncthing (WiFi) ──► │ • yt-dlp download    │
│ • Status view   │        (file sync)         │ • TF Lite tagging    │
│ • Playlist UI   │                            │ • Playlist gen       │
│ • Library       │                            │ • SQLite database    │
│                 │                            │                      │
│ Poweramp ◄──────┤ .m3u files                 │                      │
└─────────────────┘                            └──────────────────────┘
```

## Components

| Component | Tech |
|---|---|
| Backend | FastAPI + SQLite, Python 3.11 |
| Download | yt-dlp + ffmpeg + Deno |
| AI tagging | librosa → Keras → TF Lite (genre + mood) |
| File sync | Syncthing (Pi send-only → phone receive-only) |
| Remote access | Tailscale (fixed IP on any network) |
| Android | Kotlin MVVM, Retrofit 2, WorkManager |

## Setup

### Prerequisites

- Raspberry Pi 4 (4 GB RAM), Debian 13 (Trixie)
- Docker + Compose v2 plugin
- External USB SSD mounted at `/mnt/usb-ssd/media`
- Tailscale installed as system service on Pi

### Pi backend

```bash
# Clone the repository
git clone https://github.com/<your-username>/media-sync.git
cd media-sync

# Set environment variables
cp .env.example .env
# Edit .env: set API_KEY to a strong random string

# Start services
docker compose up -d
```

The API is available at `http://<tailscale-ip>:8000`.  
Syncthing web UI: `http://<tailscale-ip>:8384`.

### ML models

TF Lite models are **not** stored in this repository.  
Download from Google Drive and place in `backend/models/`:
- `backend/models/genre_classifier.tflite`
- `backend/models/mood_classifier.tflite`

*(Link to be added once models are trained in Week 6.)*

### Android app

Open `android/MediaSync/` in Android Studio.  
Set the Pi's Tailscale IP and API key in the app settings before first use.

## Development

### Backend (Python)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Lint + type check:

```bash
ruff check backend/
ruff format --check backend/
mypy backend/
pytest backend/tests/
```

### CI

GitHub Actions runs on every push:
- Ruff lint + format check
- mypy type check
- pytest with coverage report

## Legal

Personal use only. Hungarian copyright law (Act LXXVI of 1999, §35) permits private copying for natural persons. No distribution features included.
