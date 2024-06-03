class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.__first = first  # приватные атрибуты
        self.__last = last  # приватные атрибуты
        self._email = first + '.' + last + '@email.com'  # защищенный атрибут
        self.pay = pay

    def fullname(self):
        return f'{self.__first} {self.__last}'


emp_1 = Employee('Ivan', 'Ivanov', 50_000)
# print(emp_1.__first)
# print(emp_1._Employee__first)
# emp_1._Employee__first = 'Petr'
# print(emp_1._Employee__first)
print(emp_1.fullname())
print(emp_1._email)
emp_1._email = 'test@test1.com'
print(emp_1._email)
print(emp_1.pay)

"""
Пример из начала видео 

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.__first = first # приватные атрибуты
        self.__last = last # приватные атрибуты
        self._email = first + '.' + last + 'email.com' # защищенный атрибут
        self.pay = pay

    # Публичный метод, который можно вызывать от объекта
    def fullname(self):
        return f'{self.__first} {self.__last}'

    # Приватный метод, который может быть использован только внутри класса
    def __send_mail(self):
        #Фунционал отправки письма

    # Защищенный метод для использования внутри текущего класса и всех классов-наследников
    def _pay_salary(self):
        #Функционал выплаты зарплат

"""


"""
# тестирование изменения защищенного атрибута почты 

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.__first = first  # приватные атрибуты
        self.__last = last  # приватные атрибуты
        self._email = first + '.' + last + '@email.com'  # защищенный атрибут
        self.pay = pay

    def fullname(self):
        return f'{self.__first} {self.__last}'


emp_1 = Employee('Ivan', 'Ivanov', 50_000)
# print(emp_1.__first)
print(emp_1.fullname())
print(emp_1._email)
emp_1._email = 'test@test1.com'
print(emp_1._email)
print(emp_1.pay)
"""

"""
# доступ и изменение защищенного атрибута private attr 

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.__first = first  # приватные атрибуты
        self.__last = last  # приватные атрибуты
        self._email = first + '.' + last + '@email.com'  # защищенный атрибут
        self.pay = pay

    def fullname(self):
        return f'{self.__first} {self.__last}'


emp_1 = Employee('Ivan', 'Ivanov', 50_000)
# print(emp_1.__first)
print(emp_1._Employee__first)
emp_1._Employee__first = 'Petr'
print(emp_1._Employee__first)


print(emp_1._Employee__first)
emp_1._Employee__first = 'Petr'
"""