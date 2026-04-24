
<!-- Planner note GR-001 @ 2026-04-24T05:24:59.950660+00:00 -->
<## Task: GR-002 Create research notes file for testing greet
---
id: GR-002
description: Create research notes file for testing greet.
instructions: |
  Create the file `.loomstack/context/research/GR-002.md`.
  The file can be empty. Its existence is required by the main objective.
  This file is intended to hold research notes for the task of writing tests for the `greet` function.
>

<## Task: GR-003 Create tests/test_app.py and test greet
---
id: GR-003
description: Create tests/test_app.py and test the greet function.
instructions: |
  1. Create a new directory `tests`.
  2. Create a new file `tests/test_app.py`.
  3. In `tests/test_app.py`, import the `greet` function from `app.py`.
  4. Write a pytest test function called `test_greet` that asserts `greet("world")` returns `"hi world"`.
>


<!-- Planner note GR-002 @ 2026-04-24T05:26:09.227744+00:00 -->
<!-- conventions from GR-002 -->
- Adding a `.gitignore` is a good first step.
- Research notes can inform subsequent coding tasks.

