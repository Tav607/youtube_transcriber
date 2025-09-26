#!/usr/bin/env python3
"""Interactive helper script to download audio tracks from YouTube URLs."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Final, TypedDict


class FormatChoice(TypedDict):
    label: str
    value: str
    requires_ffmpeg: bool


SUPPORTED_FORMATS: Final[list[FormatChoice]] = [
    {
        "label": "webm (bestaudio, no conversion)",
        "value": "webm",
        "requires_ffmpeg": False,
    },
    {"label": "mp3", "value": "mp3", "requires_ffmpeg": True},
    {"label": "m4a", "value": "m4a", "requires_ffmpeg": True},
    {"label": "opus", "value": "opus", "requires_ffmpeg": True},
    {"label": "flac", "value": "flac", "requires_ffmpeg": True},
    {"label": "wav", "value": "wav", "requires_ffmpeg": True},
]

DEFAULT_OUTPUT_DIR = Path("output")


def prompt(message: str) -> str:
    try:
        return input(message)
    except EOFError:  # Handles Ctrl-D to avoid tracebacks in interactive use
        print("\nNo input provided. Exiting.")
        sys.exit(1)


def choose_format() -> FormatChoice:
    print("Available audio formats:")
    for idx, fmt in enumerate(SUPPORTED_FORMATS, start=1):
        print(f"  {idx}. {fmt['label']}")

    while True:
        choice = prompt("Select a format by number (default 1): ") or "1"
        if not choice.isdigit():
            print("Please enter a number from the list.")
            continue
        idx = int(choice)
        if 1 <= idx <= len(SUPPORTED_FORMATS):
            return SUPPORTED_FORMATS[idx - 1]
        print("Number out of range, please try again.")


def resolve_yt_dlp() -> str:
    """Return the yt-dlp executable, preferring the current venv."""
    python_path = Path(sys.executable)
    candidate = python_path.with_name("yt-dlp")
    if candidate.exists():
        return str(candidate)

    fallback = shutil.which("yt-dlp")
    if fallback:
        return fallback

    print("yt-dlp executable not found. Make sure the virtual environment is activated.")
    sys.exit(1)


def ensure_ffmpeg() -> None:
    """Abort early if ffmpeg/ffprobe are missing."""
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if ffmpeg and ffprobe:
        return
    print(
        "Missing ffmpeg/ffprobe. Install them first (e.g. `sudo apt install ffmpeg`) "
        "or provide their path via the --ffmpeg-location option."
    )
    sys.exit(1)


def download_audio(url: str, format_choice: FormatChoice, output_dir: Path) -> None:
    if format_choice["requires_ffmpeg"]:
        ensure_ffmpeg()

    output_dir.mkdir(parents=True, exist_ok=True)
    out_template = str(output_dir / "%(title)s.%(ext)s")

    cmd = [resolve_yt_dlp()]
    if format_choice["requires_ffmpeg"]:
        cmd.extend(
            [
                "--extract-audio",
                "--audio-format",
                format_choice["value"],
                "--audio-quality",
                "0",
            ]
        )
    else:
        # Prefer a webm audio stream without invoking ffmpeg.
        cmd.extend(["-f", "bestaudio[ext=webm]/bestaudio"])

    cmd.extend(["-o", out_template, url])

    print("\nStarting download...\n")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        print(f"yt-dlp failed with exit code {exc.returncode}.")
        sys.exit(exc.returncode)



def main() -> None:
    url = prompt("Enter the YouTube video URL: ").strip()
    if not url:
        print("URL cannot be empty.")
        sys.exit(1)

    format_choice = choose_format()

    output_dir = DEFAULT_OUTPUT_DIR
    print(f"\nAudio will be saved to: {output_dir.resolve()}\n")

    download_audio(url, format_choice, output_dir)
    print("\nDownload finished.")


if __name__ == "__main__":
    main()
