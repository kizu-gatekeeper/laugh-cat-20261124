#!/usr/bin/env python3
"""Write the cat's review of its human to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh: Cat Reviews Its Human"
bounty. The program writes exactly one line of text and nothing else.

How the line targets the judge brief (funny, fresh, tight): the review is
written in deadpan one-star marketplace voice, but the reviewer is the cat
and the product under review is the human. The joke is the power inversion
-- the human feeds, cleans and pays rent, yet the cat grades him as a
delusional service provider and still decides to keep him, the way cats
review everything: harshly, and from above.
"""

import os
from pathlib import Path

LINE = "One star. He feeds me, cleans my litter, and pays my rent, yet still believes the apartment is his. Delusional. Would keep."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
