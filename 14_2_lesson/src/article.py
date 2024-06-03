class Article:
    """ класс для хранения статьи """
    article_id: int
    title: str
    content: str

    # атрибут на уровне класса для хранения всех статей
    articles = dict()  # как хранить, чтобы быстро получать доступ, лучший вариант хранить в словаре

    def __init__(self, title, content):
        """ Конструктор для статьи """
        self.article_id = self.get_new_id()  # сразу ставим метод, чтобы получать ID
        self.title = title
        self.content = content


    #  нужен метод, который будет проходить по всем id искать последний и прибавлять 1
    def get_new_id(self) -> int:
        """ Метод для получения id следующей статьи """
        if len(self.articles) > 0:
            # должен вернуться следующий id, поэтому мы берем max + 1
            # когда артибут меняется на уровне класса, он меняется на всех объектах
            return max(self.articles.keys()) + 1
        return 1

    #  номер id все также выводится 1, все потому, что articles мы нигде не начали заполнять.
    #  метод к добавлению
    #  создается новая статья, и статья добавляется в список articles
    @classmethod
    def insert(cls, title: str, content: str):
        """ метод для создания и добавления статьи """
        # режимы доступа. Можно вместо метода, использовать класс метод ( def insert(self, title: str, content: str): -> classmwthod )
        new_article = cls(title, content)
        # т.к. мы работаем с классом, то можно обратиться
        # мы обращаемся к словарю articles, в квадратных передаем новый id и присваиваем ему значение нового id
        cls.articles[new_article.article_id] = new_article
        return new_article


    @classmethod
    def search(cls, article_id):
        """ Метод для поиска статьи по ID """
        #  Если мы пробуем метод "Утрированный путь", то мы можем в методе задать сразу значение
        #  чтобы получить ожидаемый результат теста, а потом уже оформить корректный return
        #  Утрированно -> return self.Article('1', '2') -> получаем результат проверки: '1' != 'test3'
        # return cls('test3', 'test3')
        return cls.articles[article_id]

    # потом переделываем на классметод
    # def search(self):
    #     """ Метод для поиска статьи по ID """
    #     #  Если мы пробуем метод "Утрированный путь", то мы можем в методе задать сразу значение
    #     #  чтобы получить ожидаемый результат теста, а потом уже оформить корректный return
    #     #  Утрированно -> return Article('1', '2') -> получаем результат проверки: '1' != 'test3'
    #     return  self.Article('1', '2')



if __name__ == "__main__":
    # после добавление классметода меняем Article('test1', 'test1') - > Article.insert('test1', 'test1')
    new_article_1 = Article.insert('test1', 'test1')
    print(new_article_1.article_id)

    new_article_2 = Article.insert('test2', 'test2')
    print(new_article_2.article_id)