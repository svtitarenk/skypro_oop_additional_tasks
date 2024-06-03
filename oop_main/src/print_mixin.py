class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """ шаблон: Task('Задача1', 'Описание задачи', 'Ожидает старта', '02.04.2024') """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.status}, {self.created_at}) "