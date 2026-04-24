
<!-- Planner note GR-001 @ 2026-04-24T04:52:46.434848+00:00 -->
<## Task: GR-002 Create `app.py` with a `greet` function stub
```yaml
dependencies: []
instructions: |
  1. Create a new file named `app.py`.
  2. Inside `app.py`, define a function `greet()` that takes no arguments.
  3. Make the function return the string "Hello, World!".
```
>

<## Task: GR-003 Create `tests/test_app.py` with a test for `greet`
```yaml
dependencies:
  - GR-002
instructions: |
  1. Create a new directory named `tests`.
  2. Inside `tests`, create a new file named `test_app.py`.
  3. Import the `greet` function from `app`.
  4. Write a pytest test function `test_greet` that asserts `greet()` returns "Hello, World!".
```
>

<## Task: GR-004 Create research notes file
```yaml
dependencies: []
instructions: |
  1. Create the directory path `.loomstack/context/research`.
  2. Create an empty file named `GR-002.md` inside that directory.
```
>

<!-- conventions from GR-001 -->
- Keep diffs tiny
- One function per PR
- Stdlib only
- app.py is a single file
- Tests in tests/test_app.py


<!-- Planner note GR-002 @ 2026-04-24T04:54:05.730363+00:00 -->
<## Task: GR-003 Create `app.py` and add the `greet` function
---
objective: Create the main application file and a function to be tested, as a foundation for writing tests.
prerequisites:
  - GR-001 is complete.
deliverables:
  - file_create: app.py
  - code: Add a placeholder `greet` function to `app.py`. It can `pass` or return a dummy value.
conventions:
  - Keep diffs tiny.
  - One function per PR.
>

<!-- conventions from GR-002 -->
- The failed research task (GR-002) is non-blocking; proceed with implementation.
- Create `app.py` with the `greet` function signature as the next step.

