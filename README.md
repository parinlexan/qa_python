# qa_python

test_init_genre_age_rating - метод init отдает верный список жанров недоступных детям

test_add_new_book_add_one_book_adds_book - добавление одной книги

test_add_new_book_add_two_books_adds_book - добавление двух книг

def test_add_new_book_add_symbol_length_check_adds_book - проверка граничных валидных (1, 39, 40) значений длины книги

test_add_new_book_add_same_book_doesnt_add_book - добавление книги с одним и тем же названием

test_add_new_book_41_and_0_symbol_book_doesnt_add_book - проверка граничных не валидных (0, 41) значений длины книги

test_set_book_genre_from_book_genre_adds_genre - утсановка жанра для книги

test_set_book_genre_random_string_doesnt_add_genre - отсутствие установки жанра для книги

test_get_book_genre_existing_book_gives_info - получение жанра существуюей книги

test_get_book_genre_random_string_doesnt_give_info - отсутствие информации при попытки получить жанр несуществующей книги

test_get_books_for_children_child_appropriate_genres_shows_genres - получение списка книг с разрешенным для детей жанром

test_get_books_for_children_child_inappropriate_genres_doesnt_shows_genres - отсутсвие вывода запрещнных для детей жанров

test_get_books_with_specific_genre_existed_genre_gives_books - получение существующей книги с определнным жанром

test_get_list_of_favorites_books_gives_info - получение списка любимых книг

test_add_book_in_favorites_adds_book - добавление книги в список любимых

test_delete_book_from_favorites_removes_the_book - удаление книги из списка любимых