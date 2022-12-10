from .day00 import get_message


def test_get_message() -> None:
    assert get_message() == "hello world"
