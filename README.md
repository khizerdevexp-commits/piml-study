# Physics-Informed Machine Learning Lecture Notes

This repository is built for studying a YouTube lecture series on Physics-Informed Machine Learning (PIML).

It helps you:
- extract transcripts from lecture videos
- generate structured markdown notes for each lecture
- process a full lecture series in one pass
- store paper links and references for each topic
- start small experiments in PyTorch or JAX

## Workflow

1. Add lecture metadata to `config/videos.yaml`
2. Run the batch generator
3. Each lecture becomes a standalone markdown file in `notes/`
4. Review and expand with math, diagrams, and your own insights

## Project layout

- `config/videos.yaml` — lecture list for the full series
- `config/references.yaml` — research references by topic
- `src/piml_workflow/` — core utilities
- `scripts/build_series.py` — command-line entry point
- `notes/` — generated lecture notes

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build all lecture notes

```bash
python scripts/build_series.py --config config/videos.yaml --output_dir notes
```

## Build one lecture at a time

```bash
python - <<'PY'
from src.piml_workflow.youtube_utils import fetch_transcript, build_video_url
from src.piml_workflow.note_builder import build_markdown_notes, save_markdown_note

video_id = "AEOcss20nDA"
title = "Hamiltonian Neural Networks (HNN)"
url = build_video_url(video_id)
transcript = fetch_transcript(video_id)

content = build_markdown_notes(
    video_id=video_id,
    title=title,
    topic="Hamiltonian Neural Networks",
    url=url,
    transcript_text=transcript,
    references=[
        "Greydanus, Samuel, et al. 'Hamiltonian neural networks.'",
        "Brunton, Steven L., et al. 'Machine Learning for Physics and the Physics of Learning.'",
    ],
    framework="PyTorch / JAX",
)

path = save_markdown_note("notes", title, content)
print(path)
PY
```

## Notes

This repo is designed to support your lectures, but it does not replace careful reading of the mathematical derivations and papers discussed in the videos.

Use this as a study scaffold and add your own explanations, diagrams, and experiments as you progress.
