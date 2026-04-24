#!/usr/bin/env python3
import argparse
from pathlib import Path
from yt_dlp import YoutubeDL


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="YouTube URL to download")
    parser.add_argument("--output-dir", default="downloads")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "outtmpl": str(output_dir / "%(title).200B [%(id)s].%(ext)s"),
        "format": "bv*+ba/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])


if __name__ == "__main__":
    main()
