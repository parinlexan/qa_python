import random

import pytest

from main import BooksCollector
from book_names import BookNames

class TestBooksCollector:

    def test_init_(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Ключворды')
        assert (len(collector.get_books_genre()) == 1
                and 'Ключворды' in collector.get_books_genre())

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Я', 'Чипи-чипи чапа-чапа дуби-дуби даба-даба',
                                      'Чипи-чипи чапа-чапа дуби-дуби даба-даба!'])
    def test_add_new_book_add_symbol_length_check(self, collector, name):
        collector.add_new_book(name)
        assert (len(collector.get_books_genre()) == 1
                and name in collector.get_books_genre())

    def test_add_new_book_add_same_book(self, collector):
        collector.add_new_book('Кот в сандалях')
        collector.add_new_book('Кот в сандалях')
        assert (len(collector.get_books_genre()) == 1
                and 'Кот в сандалях' in collector.get_books_genre())

    @pytest.mark.parametrize('name', ['Чипи-чипи чапа-чапа дуби-дуби даба-даба!!', ''])
    def test_add_new_book_41_and_0_symbol_book(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_from_book_genre(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre(BookNames.relaxing_book, genre)
        assert genre in list(pre_added_book.get_books_genre().values())

    def test_set_book_genre_random_string(self, pre_added_book):
        pre_added_book.set_book_genre(BookNames.relaxing_book, 'genre')
        assert list(pre_added_book.get_books_genre().values()) == ['']

    def test_get_book_genre_existing_book(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre(BookNames.relaxing_book, genre)
        assert pre_added_book.get_book_genre(BookNames.relaxing_book) == genre

    def test_get_book_genre_random_string(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre(BookNames.relaxing_book, genre)
        assert pre_added_book.get_book_genre('rrrrr') == None

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_child_appropriate_genres(self, pre_added_book, genre):
        pre_added_book.set_book_genre(BookNames.relaxing_book, genre)
        assert (pre_added_book.get_books_for_children()
                == list(pre_added_book.get_books_genre().keys()))

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_child_inappropriate_genres(self, pre_added_book, genre):
        pre_added_book.set_book_genre(BookNames.relaxing_book, genre)
        assert pre_added_book.get_books_for_children() == []

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии',
                                       'Ужасы', 'Детективы'])
    def test_get_books_with_specific_genre_existing_genre(self, collector, genre):
        collector.add_new_book(BookNames.evening_book)
        collector.set_book_genre(BookNames.evening_book, genre)
        collector.add_new_book(BookNames.dawn_book)
        collector.set_book_genre(BookNames.dawn_book, genre)
        assert (BookNames.evening_book in collector.get_books_with_specific_genre(genre)
                and BookNames.dawn_book in collector.get_books_with_specific_genre(genre))

    def test_get_list_of_favorites_books(self, pre_added_book):
        pre_added_book.add_book_in_favorites(BookNames.relaxing_book)
        assert pre_added_book.get_list_of_favorites_books() != []

    def test_add_book_in_favorites_two_books(self,collector, pre_added_book):
        collector.add_new_book(BookNames.relaxing_book)
        collector.set_book_genre(BookNames.relaxing_book, random.choice(BooksCollector().genre))
        collector.add_new_book(BookNames.history_book)
        collector.set_book_genre(BookNames.history_book, random.choice(BooksCollector().genre))
        collector.add_book_in_favorites(BookNames.relaxing_book)
        collector.add_book_in_favorites(BookNames.history_book)
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites(self, pre_added_book):
        pre_added_book.add_book_in_favorites(BookNames.relaxing_book)
        pre_added_book.delete_book_from_favorites(BookNames.relaxing_book)
        assert pre_added_book.get_list_of_favorites_books() == []