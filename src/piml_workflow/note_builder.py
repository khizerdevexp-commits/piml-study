from __future__ import annotations

from pathlib import Path
from typing import List, Optional


def sanitize_filename(title: str) -> str:
    import re
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", title.lower()).strip("_")
    return cleaned or "lecture_notes"


def make_summary_section(title: str, topic: str, url: str) -> str:
    return f"""# {title}

**Topic:** {topic}
**Video Link:** [{url}]({url})

---

## 1. Executive Summary

This lecture focuses on {topic}. Write a concise overview here:
- key idea 1
- key idea 2
- key idea 3

---

"""


def make_math_section() -> str:
    return """
## 2. Mathematical Setup

### Governing equations
Write the relevant equations here.

Example:

$$
\dot{x} = f(x, t)
$$

$$
\mathcal{L}(u, \lambda) = \int (\text{data loss} + \text{physics loss}) \, dx
$$

---

"""


def make_architecture_section(framework: str = "PyTorch / JAX") -> str:
    return f"""
## 3. Model Architecture

### Important ideas
- learn dynamics or state evolution
- impose physical constraints
- use automatic differentiation
- combine data loss with physics residual

### Frameworks used
- PyTorch: `torch.autograd`
- JAX: `jax.grad`, `jax.jacobian`

Working framework: {framework}

---

"""


def make_implementation_block() -> str:
    return """
## 4. Minimal Implementation Sketch

```python
import torch
import jax
import jax.numpy as jnp

# Skeleton for a physics-informed model

def model_loss(model, x, y):
    pred = model(x)
    data_loss = ((pred - y) ** 2).mean()
    return data_loss
```

---

"""


def make_transcript_section(transcript_text: str) -> str:
    return f"""
## 5. Lecture Transcript Highlights

```text
{transcript_text}
```

---

"""


def make_references_section(references: Optional[List[str]] = None) -> str:
    refs = references or ["Add relevant papers, notes, and references here."]
    entries = "\n".join(f"- {ref}" for ref in refs)
    return f"""
## 6. References

{entries}

---

"""


def make_takeaways_section() -> str:
    return """
## 7. Personal Takeaways

- What is the main idea?
- What is the important equation?
- What would I implement next?

---

"""


def build_markdown_notes(
    video_id: str,
    title: str,
    topic: str,
    url: str,
    transcript_text: str,
    references: Optional[List[str]] = None,
    framework: str = "PyTorch / JAX",
) -> str:
    """Build a complete lecture note in markdown."""
    doc = []
    doc.append(make_summary_section(title, topic, url))
    doc.append(make_math_section())
    doc.append(make_architecture_section(framework))
    doc.append(make_implementation_block())
    doc.append(make_transcript_section(transcript_text))
    doc.append(make_references_section(references))
    doc.append(make_takeaways_section())
    return "\n".join(doc)


def save_markdown_note(output_dir: str, title: str, content: str) -> str:
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = sanitize_filename(title)
    file_path = out_dir / f"{slug}.md"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)
