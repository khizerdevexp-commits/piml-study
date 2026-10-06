import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.piml_workflow.series_builder import build_series_notes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate markdown lecture notes for a Physics-Informed ML video series."
    )
    parser.add_argument("--config", type=str, required=True, help="Path to videos.yaml")
    parser.add_argument(
        "--output_dir",
        type=str,
        default="notes",
        help="Directory to save generated lecture notes",
    )
    args = parser.parse_args()

    files = build_series_notes(args.config, args.output_dir)
    print("Generated files:")
    for path in files:
        print(path)


if __name__ == "__main__":
    main()
