import pytest

from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def pre_added_book():
    collector = BooksCollector()
    collector.add_new_book('История чилибони')
    return collector