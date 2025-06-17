import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture
    def empty_collector(self):
        # Новый пустой объект BooksCollector
        return BooksCollector()

    @pytest.fixture
    def filled_collector(self):
        # Заполнение
        bc = BooksCollector()
        bc.add_new_book('Книга №1')
        bc.set_book_genre('Книга №1', 'Фантастика')

        bc.add_new_book('Книга №2')
        bc.set_book_genre('Книга №2', 'Ужасы')

        bc.add_new_book('Книга №3')
        bc.set_book_genre('Книга №3', 'Детективы')
        return bc

    # добавление новой книги
    def test_add_new_book_success(self, empty_collector):
        empty_collector.add_new_book('Новая книга')
        assert 'Новая книга' in empty_collector.get_books_genre()

    @pytest.mark.parametrize(
        'bad_name',
        ['', 'A' * 41]  # пустое имя и > 40 символов
    )
    def test_add_new_book_wrong_name_not_added(self, empty_collector, bad_name):
        empty_collector.add_new_book(bad_name)
        assert bad_name not in empty_collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self, empty_collector):
        empty_collector.add_new_book('Книга')
        empty_collector.add_new_book('Книга')  # дубль
        assert len(empty_collector.get_books_genre()) == 1

    # установка жанра книги
    def test_set_book_genre_success(self, empty_collector):
        empty_collector.add_new_book('Книга-жанр')
        empty_collector.set_book_genre('Книга-жанр', 'Комедии')
        assert empty_collector.get_book_genre('Книга-жанр') == 'Комедии'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Несуществующая', 'Комедии'),      # книги нет
            ('Книга-жанр',      'Не жанр')      # жанра нет
        ]
    )
    def test_set_book_genre_wrong_data_no_change(self, empty_collector, name, genre):
        empty_collector.add_new_book('Книга-жанр')
        empty_collector.set_book_genre(name, genre)
        assert empty_collector.get_book_genre('Книга-жанр') in ('', None)

    # получение книг определенного жанра
    @pytest.mark.parametrize(
        'genre, expected',
        [
            ('Фантастика', ['Книга №1']),
            ('Ужасы',      ['Книга №2']),
            ('Мультфильмы', [])  # жанр есть в справочнике, книг нет
        ]
    )
    def test_get_books_with_specific_genre(self, filled_collector, genre, expected):
        assert filled_collector.get_books_with_specific_genre(genre) == expected

    # получение книг для детей
    def test_get_books_for_children_excludes_age_rating(self, filled_collector):
        # 'Ужасы' и 'Детективы' должны быть отфильтрованы
        assert filled_collector.get_books_for_children() == ['Книга №1']

    # избранные книги
    def test_add_book_in_favorites_only_once(self, filled_collector):
        filled_collector.add_book_in_favorites('Книга №1')
        filled_collector.add_book_in_favorites('Книга №1')          # повторно
        assert filled_collector.get_list_of_favorites_books() == ['Книга №1']

    def test_delete_book_from_favorites(self, filled_collector):
        filled_collector.add_book_in_favorites('Книга №1')
        filled_collector.delete_book_from_favorites('Книга №1')
        assert filled_collector.get_list_of_favorites_books() == []

    # получение списка избранных книг
    def test_get_list_of_favorites_books_returns_list_type(self, empty_collector):
        assert isinstance(empty_collector.get_list_of_favorites_books(), list)
