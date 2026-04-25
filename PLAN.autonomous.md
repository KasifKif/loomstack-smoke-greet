
<!-- Planner note GR-003 @ 2026-04-25T01:39:18.479127+00:00 -->
<## Task: GR-004 Add a unit test for the greet function
plan:
  - "Create the `tests/` directory if it does not already exist."
  - "Create a new file `tests/test_app.py`."
  - "In the new file, import the `greet` function from the `app` module."
  - "Add a test function `test_greet` that asserts `greet('World')` returns 'Hello, World!' as expected."
>

<!-- conventions from GR-003 -->
- Tests must be placed in `tests/test_app.py` to be discovered by the test runner.


<!-- Planner note GR-001 @ 2026-04-25T01:39:37.555795+00:00 -->
## Task: GR-003 Add unit tests for the greet function.
```yaml
id: GR-003
description: Add unit tests for the greet function.
dependencies: [GR-001]
```


<!-- Planner note GR-002 @ 2026-04-25T01:40:12.855676+00:00 -->
<## Task: GR-003 Implement the greet function in app.py
id: GR-003
description: Implement the greet function in app.py
body: |
  Create the file `app.py` and add a `greet` function.

  The function should take a `name` string and return "Hello, {name}!".

  ```python
  # app.py
  def greet(name: str) -> str:
      return f"Hello, {name}!"
  ```
>

<!-- conventions from GR-002 -->
- One function per PR.


<!-- Planner note GR-003 @ 2026-04-25T01:40:44.662295+00:00 -->
## Task: GR-004 Add a unit test for the `greet` function.
---
```yaml
task: GR-004
description: Add a unit test for the `greet` function.
details:
  - The previous attempt (GR-003) failed to create the test file.
  - Create a new file at `tests/test_app.py`.
  - Inside this file, import the `greet` function from `app.py`.
  - Write a `pytest` test function named `test_greet`.
  - The test should assert that `greet()` returns the string "Hello, World!".
```

