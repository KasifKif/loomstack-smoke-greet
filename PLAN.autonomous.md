
<!-- Planner note GR-001 @ 2026-04-25T01:45:27.522037+00:00 -->
<## Task: GR-002 Add test for greet function
```yaml
id: GR-002
title: Add test for greet function
description: |
  Create the test file `tests/test_app.py`.
  Add a pytest test case for the `greet` function in `app.py`.
  The test should verify that `greet("world")` returns "hi world".
```
>


<!-- Planner note GR-002 @ 2026-04-25T01:46:18.747016+00:00 -->
<## Task: GR-003 Create app.py with a greet function
description: |
  Create the main application file `app.py`.
  Add a simple `greet` function that takes a name and returns a greeting string.
  This is the first step towards fulfilling the main objective.
>

<!-- conventions from GR-002 -->
- Keep changes minimal, one function at a time.


<!-- Planner note GR-003 @ 2026-04-25T01:47:34.216313+00:00 -->
<## Task: GR-004 Create tests/test_app.py and add a unit test for the greet function.
path: tests/test_app.py
action: create
content: |
  from app import greet

  def test_greet():
      assert greet("World") == "Hello, World!"
##>

<!-- conventions from GR-003 -->
- Tests go in tests/test_app.py, use pytest.

