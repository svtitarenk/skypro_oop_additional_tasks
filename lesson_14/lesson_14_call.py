"""
ЗАДАЧА
Сделать класс с экземплярами, содержащими символы, которые надо удалять из строки.
Эта строка должна передаваться в качестве аргумента к экземпляру класса

1 Создать класс
2 Реализовать метод __init__
3 Реализовать метод __call__
"""


class StripChars:
    """Класс, удаляющий определенные символы из строки"""

    def __init__(self, chars):
        """Инициализация символов для удаления"""
        self.chars = chars

    def __call__(self, *args, **kwargs):
        """Удаление символов из строки"""
        return args[0].strip(self.chars)
    # args[0] - потому что мы передаем не именованные аргументы, а так можно было бы


# Cоздаем два экземпляра класса StripChars: st1 и st2
# st1 = StripChars('?')
# # st2 = StripChars('_')
#
# res = st1('?Example?')
#
# print(res)  # Example


# ----------------------------------------------------------
"""
# вариант 1, когда нет переменных
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.__counter += 1
        return self.__counter


c = Counter()
c2 = Counter()
c()
c()
res = c()
res2 = c2()
print(res, res2)
"""

# ----------------------------------------------------------
"""
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step  # передаем переменную step
        return self.__counter


c = Counter()
c2 = Counter()
c()
c(2)  # прописываем произвольно
res = c(10)  # прописываем произвольно
res2 = c2(-5)  # прописываем произвольно
print(res, res2)
"""

# ----------------------------------------------------------
"""Зачем это нужно и где может пригодиться"""

"""
class StripChars2:  # берем пример, где будем удалять символы
    def __init__(self, chars):  # chars (прописываем символы, которые будем удалять из строки)
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):  # если элемент не является строкой, то выведем исключение
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)  # а иначе вернем результат обработки этой строки


s1 = StripChars2("?:!.; ")
s2 = StripChars2(" ")  # создадим экземпляр, который будет удалять толкько пробелы
res = s1(" Hello world! ")
res2 = s2(" Hello world! ")
print(res, res2, sep="\n")
"""

# ----------------------------------------------------------
"""Используем функцию, для вызова другой функции"""
import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


#df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))
