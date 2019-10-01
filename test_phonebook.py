from phonebook import PhoneBook
import pytest

@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty Phonebook object"
    phonebook = PhoneBook(tmpdir)
    yield phonebook
    phonebook.clear()


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
