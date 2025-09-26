# YouTube Audio Downloader

This project ships with an interactive Python script that downloads audio from a single YouTube URL. By default it grabs the best available `webm` audio stream so `ffmpeg` is not required; if you pick another format the script will invoke `ffmpeg` to transcode.

## Requirements

- Python 3.12+
- `yt-dlp`
- Optional: `ffmpeg` (needed whenever you select a non-`webm` output)

## Quick Start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install yt-dlp
python download_audio.py
```

When the script runs:
1. Enter the target YouTube video URL.
2. Choose the desired output format (default is `webm`).
3. The file is written to the `output/` directory using the video title as the filename.

## Troubleshooting

- **Missing ffmpeg**: If `mp3`, `m4a`, etc. fail with a message about `ffmpeg/ffprobe`, install the tools first: `sudo apt install ffmpeg`.
- **Download errors**: YouTube changes its APIs occasionally. Update `yt-dlp` before retrying: `pip install --upgrade yt-dlp`.

## Project Layout

- `download_audio.py`: interactive downloader script.
- `output/`: default directory for downloaded media (safe to clean up).
- `README.md`: project overview.
- `AGENTS.md`: automation playbook.

## Next Steps

- Add an API-powered transcription workflow that can process downloaded audio automatically.
