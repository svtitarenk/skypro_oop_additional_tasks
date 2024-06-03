#RecurrsionError - ошибка рекурсии - def recursion():return recursion
#TypeError - Ошибка типа - 2+'2'
#OverflowError - Ошибка переполнения - math.exp(1000)
#AssertionError - a,b = 1, 'a'; asser a == b

# try:
#     print(a)
# except NameError:
#     print('Обращение к несуществующей переменной')
#
# try:
#     1 / 0
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
#
# try:
#     open('some_file')
# except FileNotFoundError:
#     print('Файл не существует')


""" задача, спровоцировать и обработать исключения разных типов """
#NameError
#ZeroDivisionError
#FileNotFoundError

# try:
#     # print(a)
#     # 1 / 0
#     open("some_file")
# except FileNotFoundError:
#     print('file not found')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except NameError:
#     print('Обращение к несуществующей переменной')

""" Иерархия исключения """

# try:
#     print(a)
#     # основной код
# except NameError:
#     # Код, если возникло исключение
#     print('Second try')
# else:
#     # Код, если не возникло исключений и код в бллоке try был выполнен.
#     print('Third try')
# finally:
#     # Код, который выполняется всегда
#     print('Finally try')


""" пробуем на практике иерархию исключений """

# try:
#     a, b = input('Введите числа: ').split()
#     a, b = int(a), int(b)
#     result = a / b
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print('Операция завершена')

""" Практика """

""" Задача. Принять на вход от пользователя 2 числа a и b.
Разделить a на b. Убедиться, что пользователь ввел числа и эти числа целые. Число b должно быть отличным от нуля
"""
try:
    a, b = input('введите числа через пробел: ').split()
    a, b = int(a), int(b)
    result = a / b
except TypeError as e:
    print('TypeError', e)
# except Exception as e:
#     print(e)
except ValueError as e:
    print('ValueError', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
else:
    print('result', result)
finally:
    print('операция завершена')
