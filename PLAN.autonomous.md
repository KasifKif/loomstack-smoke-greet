
<!-- Planner note GR-001 @ 2026-04-25T01:36:21.949206+00:00 -->
<## Task: GR-002 Add a unit test for the greet function

task: GR-002
description: |
  Add a unit test for the `greet` function in `app.py`.
  Create the `tests/test_app.py` file and add a test case that asserts `greet("world")` returns `"hi world"`.
dependencies:
  - GR-001
>


<!-- Planner note GR-002 @ 2026-04-25T01:37:14.471077+00:00 -->
<## Task: GR-003 Add greet function to app.py
---
body: |
  Add a `greet` function to `app.py`.

  It should take a `name` string argument and return the string "Hello, {name}!".
dependencies:
  - GR-001
>

<!-- conventions from GR-002 -->
- One function per PR.
- Keep diffs tiny.


<!-- Planner note GR-003 @ 2026-04-25T01:38:15.107200+00:00 -->
## Task: GR-004 Add a unit test for the greet function
file: tests/test_app.py
content: |
  from app import greet

  def test_greet():
      assert greet("World") == "Hello, World!"

<!-- conventions from GR-003 -->
- Tests must be placed in `tests/test_app.py`.

