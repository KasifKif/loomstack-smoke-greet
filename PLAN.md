# Greet demo — autonomous-loop smoke test

Main objective: `greet(name)` exists in `app.py` and returns `f"hi {name}"`,
with a passing unit test.

## Task: GR-001 scaffold app.py with a greet stub

role: code_worker
required: true
context_files:
  - app.py
acceptance:
  - file exists: app.py
  - function exists: greet in app.py
notes: |
  Create app.py at the repo root with a function signature
  `def greet(name: str) -> str:` and a trivial body that returns
  `f"hi {name}"`. No tests yet — GR-003 adds those.

## Task: GR-002 collect pytest test patterns

role: researcher
needs_research: true
depends_on: [GR-001]
acceptance:
  - task_completed: GR-002
notes: |
  Summarise common pytest patterns for testing single-function modules
  into the researcher's notes file. 5-10 bullet points is plenty — this
  is reference material for GR-003, not a treatise. The Researcher writes
  to ``state_dir/context/research/<task-id>.md`` (loomstack state, not a
  project file), so the acceptance criterion is intentionally non-literal
  and references task completion only — the Planner LLM evaluates against
  ``done_ids`` (which it sees in the prompt) rather than trying to verify
  the research notes from a downstream task's diff.

## Task: GR-003 add a unit test for greet

role: code_worker
required: true
depends_on: [GR-001, GR-002]
architect_preapproved: true
architect_budget_usd: 1.00
context_files:
  - tests/test_app.py
acceptance:
  - file exists: tests/test_app.py
  - tests_pass: unit
notes: |
  Write tests/test_app.py with a pytest test that calls greet("world")
  and asserts the result equals "hi world". Keep it one test function.
