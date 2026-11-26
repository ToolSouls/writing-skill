#!/usr/bin/env python3
"""Generate a stable per-article layout variation signature."""

from __future__ import annotations

import argparse
import hashlib
import json


TYPES = {
    "tutorial": ["tutorial-a", "tutorial-b", "tutorial-c"],
    "analysis": ["analysis-a", "analysis-b", "analysis-c"],
    "listicle": ["listicle-a", "listicle-b", "listicle-c"],
    "review": ["review-a", "review-b", "review-c"],
    "case": ["case-a", "case-b", "case-c"],
    "story": ["story-a", "story-b", "story-c"],
    "report": ["report-a", "report-b", "report-c"],
    "essay": ["essay-a", "essay-b", "essay-c"],
}

OPENINGS = ["conclusion", "scene", "question", "data"]
TOCS = ["full", "compact", "none"]
RHYTHMS = ["even", "case-first", "question-progression", "step-progression"]
EMPHASIS = ["one-anchor-per-section", "two-anchors-per-section", "sparse"]
MEDIA = ["after-intro", "after-second-section", "between-arguments", "none"]
ENDINGS = ["summary", "checklist", "open-question", "forward-looking"]
DENSITY = ["light", "medium", "dense"]


def pick(seed: bytes, salt: int, values: list[str]) -> str:
    return values[seed[salt % len(seed)] % len(values)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("title")
    parser.add_argument("article_type", choices=sorted(TYPES))
    parser.add_argument("theme_id", nargs="?", default="")
    args = parser.parse_args()

    raw = f"{args.title.strip()}|{args.article_type}|{args.theme_id.strip()}".encode(
        "utf-8"
    )
    seed = hashlib.sha256(raw).digest()
    result = {
        "layout_id": pick(seed, 0, TYPES[args.article_type]),
        "opening": pick(seed, 1, OPENINGS),
        "toc": pick(seed, 2, TOCS),
        "heading_rhythm": pick(seed, 3, RHYTHMS),
        "emphasis": pick(seed, 4, EMPHASIS),
        "media_cadence": pick(seed, 5, MEDIA),
        "ending": pick(seed, 6, ENDINGS),
        "density": pick(seed, 7, DENSITY),
        "seed": seed.hex()[:16],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
