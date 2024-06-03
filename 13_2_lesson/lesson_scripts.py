import random


def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        return result_int
    return inner


@my_decorator
def get_rand_numbers():
    return random.randint(1, 100) / random.randint(1, 100)


print(get_rand_numbers())

"""
5 минута видео (пример args и kwargs)
def add_one(x):
    return x + 1


params = {'x': 10}
y = add_one(**params)
y = add_one(x=10)

"""


"""
9:00 минута видео
# создали декоратор printing в него мы принимаем на вход функцию func, которую вызываем
# через new_f
# внутри printing у нас есть вложенная функция и она принимает на вход те аргументы, которые у нас были 
# переданы на входе функции
# мы вызываем фнукцию, делаем что-то с ней и выдаем результат 
def printing(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


def add_one(x):
    return x + 1


new_f = printing(add_one)

y = new_f(10)

print(y)
"""


"""
12:30 видео. Оборачиваем в декоратор @printing нашу функцию, и декоратор работает уже через другую запись

def printing(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'func {func} called with result {result}')
        return result
    return inner


@printing
def add_one(x):
    return x + 1


y = add_one(10)
print(y)
"""


"""
16:51 добавляем декоратор в функцию и дописываем декоратор, модифицируем оборачиваемость в int result

import random


def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        return result_int
    return inner


@my_decorator
def get_rand_numbers():
    return random.randint(1, 100) / random.randint(1, 100)


print(get_rand_numbers())
"""