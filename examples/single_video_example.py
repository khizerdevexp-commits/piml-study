from src.piml_workflow.note_builder import build_markdown_notes, save_markdown_note
from src.piml_workflow.youtube_utils import build_video_url, fetch_transcript

VIDEO_ID = "AEOcss20nDA"
TOPIC = "Hamiltonian Neural Networks"
TITLE = "Hamiltonian Neural Networks (HNN)"
URL = build_video_url(VIDEO_ID)

transcript = fetch_transcript(VIDEO_ID)
content = build_markdown_notes(
    video_id=VIDEO_ID,
    title=TITLE,
    topic=TOPIC,
    url=URL,
    transcript_text=transcript,
    references=[
        "Greydanus, Samuel, et al. 'Hamiltonian neural networks.'",
        "Brunton, Steven L., et al. 'Machine Learning for Physics and the Physics of Learning.'",
    ],
    framework="PyTorch / JAX",
)

path = save_markdown_note("notes", TITLE, content)
print(f"Saved note to: {path}")
