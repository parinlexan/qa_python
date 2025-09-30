import random

import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_one_book_adds_book(self, collector):
        collector.add_new_book('Ключворды')

        assert len(collector.get_books_genre()) == 1 and 'Ключворды' in collector.get_books_genre()

    def test_add_new_book_add_two_books_adds_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Я', 'Чипи-чипи чапа-чапа дуби-дуби даба-даба', 'Чипи-чипи чапа-чапа дуби-дуби даба-даба!'])
    def test_add_new_book_add_symbol_length_check_adds_book(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 1 and name in collector.get_books_genre()

    def test_add_new_book_add_same_book_doesnt_add_book(self, collector):
        collector.add_new_book('Кот в сандалях')
        collector.add_new_book('Кот в сандалях')

        assert len(collector.get_books_genre()) == 1 and 'Кот в сандалях' in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['Чипи-чипи чапа-чапа дуби-дуби даба-даба!!', ''])
    def test_add_new_book_41_and_0_symbol_book_doesnt_add_book(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0



    def test_set_book_genre_from_book_genre_adds_genre(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre('История чилибони', genre)

        assert genre in list(pre_added_book.get_books_genre().values())

    def test_set_book_genre_random_string_doesnt_add_genre(self, pre_added_book):
        pre_added_book.set_book_genre('История чилибони', 'genre')

        assert list(pre_added_book.get_books_genre().values()) == ['']


    def test_get_book_genre_existing_book_gives_info(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre('История чилибони', genre)

        assert pre_added_book.get_book_genre('История чилибони') == genre

    def test_get_book_genre_random_string_doesnt_give_info(self, pre_added_book):
        genre = random.choice(BooksCollector().genre)
        pre_added_book.set_book_genre('История чилибони', genre)

        assert pre_added_book.get_book_genre('rrrrr') == None



    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_child_appropriate_genres_shows_genres(self, pre_added_book, genre):
        pre_added_book.set_book_genre('История чилибони', genre)

        assert pre_added_book.get_books_for_children() == list(pre_added_book.get_books_genre().keys())

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_child_inappropriate_genres_doesnt_shows_genres(self, pre_added_book, genre):
        pre_added_book.set_book_genre('История чилибони', genre)

        assert pre_added_book.get_books_for_children() == []



    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии', 'Ужасы', 'Детективы'])
    def test_get_books_with_specific_genre_existed_genre_gives_books(self, collector, genre):
        collector.add_new_book('Сумерки')
        collector.set_book_genre('Сумерки', random.choice(BooksCollector().genre))
        collector.add_new_book('Рассвет')
        collector.set_book_genre('Рассвет', genre)

        assert 'Сумерки' in collector.get_books_with_specific_genre(genre) or 'Рассвет' in collector.get_books_with_specific_genre(genre)


    def test_get_list_of_favorites_books_gives_info(self, pre_added_book):
        pre_added_book.add_book_in_favorites('История чилибони')

        assert pre_added_book.get_list_of_favorites_books() != []

    def test_add_book_in_favorites_adds_book(self, pre_added_book):
        pre_added_book.add_book_in_favorites('История чилибони')

        assert pre_added_book.get_list_of_favorites_books() != []

    def test_delete_book_from_favorites_removes_the_book(self, pre_added_book):
        pre_added_book.add_book_in_favorites('История чилибони')
        pre_added_book.delete_book_from_favorites('История чилибони')

        assert pre_added_book.get_list_of_favorites_books() == []