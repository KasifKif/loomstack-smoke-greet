from app import greet


def test_greet_world():
    assert greet("world") == "hi world"
