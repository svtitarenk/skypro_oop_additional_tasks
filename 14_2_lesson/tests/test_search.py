import pytest
from src.article import Article


@pytest.fixture
def list_articles():
    """ наполняем наш список статьями
    Потому что мы при тестировании будем проверять, сработал ли поиск по ID
    """
    Article.articles = dict()  #  важно зачистить список, чтобы тест проходил чисто, т.к. в других тестах могут передваться другие значения в словарь
    Article.insert('test1', 'test1')  # копипаст с one_article
    Article.insert('test2', 'test2')  # копипаст с one_article
    Article.insert('test3', 'test3')  # копипаст с one_article
    Article.insert('test4', 'test4')  # копипаст с one_article
    Article.insert('test5', 'test5')  # return тут можно не ставить


def test_search_3(list_articles):
    """ передаем статью для поиска и проверяем поиск
    Тестирование поиска статьи по ID
    но сравниваем не ID & ID, а сравниваем ID и заголовок передаваемой статьи
    """
    searchable_articles = Article.search(3)
    assert searchable_articles.title == 'test3'


def test_search_4(list_articles):
    """ передаем статью для поиска и проверяем поиск
    Тестирование поиска статьи по ID
    но сравниваем не ID & ID, а сравниваем ID и заголовок передаваемой статьи
    """
    searchable_articles = Article.search(4)
    assert searchable_articles.title == 'test4'
