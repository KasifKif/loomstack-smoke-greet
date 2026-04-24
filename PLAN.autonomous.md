
<!-- Planner note GR-001 @ 2026-04-24T06:18:26.675305+00:00 -->
<## Task: GR-002 Write a unit test for the greet function.
---
id: GR-002
desc: Write a unit test for the greet function.
instructions: |
  - Create a new file `tests/test_app.py`.
  - Import the `greet` function from the `app` module.
  - Write a `pytest` test case named `test_greet`.
  - The test should assert that `greet("world")` returns "hi world".
---
>

<## Task: GR-003 Create research notes for testing the greet function.
---
id: GR-003
desc: Create research notes for testing the greet function.
instructions: |
  - Create a new file at `.loomstack/context/research/GR-002.md`.
  - The file should contain notes on how to approach testing the `greet` function for task GR-002.
  - Explain that the test will use `pytest`, be located in `tests/test_app.py`, and will check the output of the `greet` function.
---
>


<!-- Planner note GR-002 @ 2026-04-24T06:19:22.062756+00:00 -->
## Task: GR-003 Implement the `greet` function and a basic test
---
description: |
  Implement the `greet` function in `app.py`.
  It should take a `name` string and return "Hello, {name}!".
  Also, add a corresponding test in `tests/test_app.py` to verify this behaviour.
  This will satisfy the main objective criteria for the function and its test.
prerequisites:
  - GR-001
  - GR-002

<!-- conventions from GR-002 -->
- Focus on implementing just the `greet` function and its test, per the 'one function per PR' rule.

