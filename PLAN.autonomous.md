
<!-- Planner note GR-001 @ 2026-04-25T01:19:11.793685+00:00 -->
<## Task: GR-002 Research salutations for the greet function + YAML body
id: GR-002
desc: Research salutations for the greet function
instructions: |
  The `greet` function currently uses a hardcoded "hi".
  Research alternative salutations (e.g., "Hello", "Greetings").
  Document your findings in a new file: `.loomstack/context/research/GR-002.md`.
  The file should contain a short list of potential salutations.
>

<## Task: GR-003 Add a unit test for the greet function + YAML body
id: GR-003
desc: Add a unit test for the greet function
instructions: |
  Create the test file `tests/test_app.py`.
  Add a `pytest` unit test for the existing `app.greet` function.
  The test should verify that `greet("world")` returns "hi world".
>


<!-- Planner note GR-002 @ 2026-04-25T01:20:00.440376+00:00 -->
<## Task: GR-003 Create app.py with a greet function
description: Create the main application file `app.py` and add a simple `greet` function to it. The function should take no arguments and return the string "Hello, World!".
##>

