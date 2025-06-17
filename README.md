# qa_python

# Тесты для BooksCollector

| Тест                                                | Проверяемое поведение                                    |
|----------------------------------------------------|----------------------------------------------------------|
| `test_add_new_book_add_two_books`                  | пример теста - добавление двух книг                     |
| `test_add_new_book_success`                        | успешное добавление новой книги                         |
| `test_add_new_book_wrong_name_not_added`           | отказ при некорректном имени (пустое или >40 символов)  |
| `test_add_new_book_duplicate_not_added`            | отказ при попытке добавить дубль                        |
| `test_set_book_genre_success`                      | успешная установка жанра книги                          |
| `test_set_book_genre_wrong_data_no_change`         | игнорирование некорректных данных при установке жанра   |
| `test_get_books_with_specific_genre`               | фильтрация книг по жанру (параметризованный тест)       |
| `test_get_books_for_children_excludes_age_rating`  | исключение книг с возрастным рейтингом из детских       |
| `test_add_book_in_favorites_only_once`             | книга добавляется в избранное только один раз           |
| `test_delete_book_from_favorites`                  | удаление книги из избранного                            |
| `test_get_list_of_favorites_books_returns_list_type` | возвращает тип `list`                                  |
