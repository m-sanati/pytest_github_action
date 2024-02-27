import pytest

from main import Person


@pytest.fixture
def person():
    return Person(name="Mahsa", age=27)


def test_person(person):
    assert person.name == "Mahsa"
    assert person.age == 27
