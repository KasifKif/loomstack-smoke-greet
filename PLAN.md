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

## Task: SEC-001 exercise security-tag escalation

role: code_worker
required: false
tags:
  - security
acceptance:
  - file exists: app.py
notes: |
  Smoke coverage for the policy's ARCHITECT_NEEDED event. The
  ``security`` tag fires ARCHITECT_NEEDED at the top of _dispatch_one;
  the default policy maps that to MARK_BLOCKED_NOTIFY at attempt 1, so
  this task never reaches an agent — it lands in BLOCKED with a Discord
  alert. ``required: false`` so the main objective still completes.

## Task: ESC-001 exercise CODE_FAIL → architect escalation

role: code_worker
required: false
acceptance:
  - file exists: app.py
notes: |
  Smoke coverage for the policy's CODE_FAIL → ESCALATE_ARCHITECT path.
  The harness pre-seeds this task's run-file with retry_count=2 +
  status=failed, so the next dispatch fires CODE_FAIL at attempt 3 →
  ESCALATE_ARCHITECT (default policy). _run_architect_review fires
  (chat_runner if configured, alert-only otherwise) and the architect
  approval gate then blocks the task.

  Acceptance reuses GR-001's ``file exists: app.py`` deliberately:
  ``_extract_main_criteria(plan)`` unions every task's acceptance into
  the planner's termination check, and the literal cross-check
  (``git cat-file -e``) on an unsatisfiable criterion would prevent
  ``main_objective_complete`` from ever firing. The dispatcher's
  CODE_FAIL flow triggers off the pre-seeded ``status: failed``, not
  ``acceptance``, so reusing a benign criterion doesn't weaken the
  escalation coverage.
