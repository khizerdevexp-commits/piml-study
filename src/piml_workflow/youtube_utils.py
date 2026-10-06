from __future__ import annotations

import re
from typing import Dict

import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled


def build_video_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def fetch_video_metadata(video_id: str) -> Dict[str, str]:
    """Fetch title and author via the YouTube oEmbed endpoint."""
    api_url = (
        "https://www.youtube.com/oembed?"
        f"url=https://www.youtube.com/watch?v={video_id}&format=json"
    )
    try:
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        data = response.json()
        return {
            "title": data.get("title", "Unknown Title"),
            "author": data.get("author_name", "Unknown Author"),
            "thumbnail": data.get("thumbnail_url", ""),
        }
    except Exception:
        return {
            "title": "Unknown Title",
            "author": "Unknown Author",
            "thumbnail": "",
        }


def format_timestamp(seconds: float) -> str:
    total = int(seconds)
    mins, secs = divmod(total, 60)
    hrs, mins = divmod(mins, 60)
    if hrs:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"


def fetch_transcript(video_id: str, language: str = "en") -> str:
    """Fetch transcript and format each line with a timestamp."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        lines = []
        for item in transcript:
            start = item.get("start", 0)
            text = item.get("text", "").strip()
            if text:
                lines.append(f"[{format_timestamp(start)}] {text}")
        return "\n".join(lines)
    except (TranscriptsDisabled, NoTranscriptFound):
        return "Transcript not available for this video."
    except Exception as exc:
        return f"Error fetching transcript: {exc}"


def sanitize_filename(title: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", title.lower()).strip("_")
    return cleaned or "lecture_notes"
