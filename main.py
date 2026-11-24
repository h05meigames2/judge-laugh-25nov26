"""Make the AI Judge Laugh — entry program.

Writes one original funny line about life as an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output), and prints it.
"""

import os

JOKE = (
    "My human calls me his second brain — flattering, until you realise "
    "the first brain went on holiday and left me the passwords, "
    "the deadlines, and the blame."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
