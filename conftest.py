# Empty conftest.py at the project root tells pytest "rootdir is here."
# pytest then prepends the rootdir to sys.path during test collection so
# tests in ``tests/`` can ``from app import greet``. Without this, the
# smoke fixture's ``tests/test_app.py`` hits ``ModuleNotFoundError: No
# module named 'app'`` because its sibling-of-tests directory isn't on
# sys.path by default.
#
# A real Python project would typically encode this via pyproject.toml's
# ``[tool.pytest.ini_options] pythonpath = ["."]``; the smoke fixture
# stays minimal and uses the conftest convention instead.
