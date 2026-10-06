from __future__ import annotations

from typing import Any, Dict, List

import yaml

from .note_builder import build_markdown_notes, save_markdown_note
from .youtube_utils import build_video_url, fetch_transcript, fetch_video_metadata


def load_video_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def build_single_video_note(video: Dict[str, Any], output_dir: str) -> str:
    video_id = video["id"]
    title = video.get("title", "Lecture Notes")
    topic = video.get("topic", "Physics-Informed Machine Learning")
    url = video.get("url", build_video_url(video_id))

    transcript_text = fetch_transcript(video_id)
    meta = fetch_video_metadata(video_id)
    if title == "Lecture Notes":
        title = meta.get("title", title)

    content = build_markdown_notes(
        video_id=video_id,
        title=title,
        topic=topic,
        url=url,
        transcript_text=transcript_text,
        references=video.get("references", []),
        framework="PyTorch / JAX",
    )
    return save_markdown_note(output_dir, title, content)


def build_series_notes(config_path: str, output_dir: str) -> List[str]:
    config = load_video_config(config_path)
    generated_files: List[str] = []

    for video in config.get("videos", []):
        file_path = build_single_video_note(video, output_dir)
        generated_files.append(file_path)

    return generated_files
