# YouTube Downloader

A simple command-line tool for downloading YouTube videos as MP3 files using yt-dlp and FFmpeg.

## Requirements

- Python 3.6+
- FFmpeg (must be in your system PATH)
- yt-dlp

## Installation

1. Clone this repository
2. Install dependencies: `pip install yt-dlp`
3. Install FFmpeg:
   - **Windows**: Download from https://www.ffmpeg.org/ or use Chocolatey: `choco install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (or equivalent for your package manager)

## Usage

Basic usage to download a single video: `python "yt downloader.py" https://www.youtube.com/watch?v=example`
Multiple videos: `python "yt downloader.py" https://www.youtube.com/watch?v=video1 https://www.youtube.com/watch?v=video2`
