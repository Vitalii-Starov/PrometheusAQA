import pytest


class User:

    def __init__(self) -> None:
        self.name = "Vitalii"
        self.second_name = "Starov"


@pytest.fixture
def user():
    yield User()


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == "Vitalii"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Starov"
