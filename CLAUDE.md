# Project conventions

## What this project is

A single-file demonstration app used by Loomstack's autonomous-loop smoke test.
Nothing here is production.

## Rules

- Python 3.11+.
- Keep `app.py` a single file. No subpackages for this project.
- Tests go in `tests/test_app.py`, use `pytest`.
- Keep diffs tiny — each PR adds or changes one small piece of behaviour.
- Don't add dependencies. Stdlib only.
- One function per PR. Don't bundle.
