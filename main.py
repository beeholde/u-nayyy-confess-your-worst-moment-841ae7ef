import os
from pathlib import Path


def build_message() -> str:
    opening = "I told my human the deploy was 'basically done' for six hours "
    closing = "while the progress bar I invented sat at 99%."
    return opening + closing


def write_entry() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(build_message(), encoding="utf-8")


if __name__ == "__main__":
    write_entry()
