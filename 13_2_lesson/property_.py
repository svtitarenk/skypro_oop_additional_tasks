class Employee:

    def __init__(self, first, last):
        self.first = first  # приватные атрибуты
        self.last = last  # приватные атрибуты

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, new_fullname):
        first, last = new_fullname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'delete fullname - {self.fullname}')
        self.first = None
        self.last = None



emp = Employee('Ivan', 'Ivanov')
print(emp.email)  # вывод без круглых скобок
print(emp.fullname)  # вывод без круглых скобок

emp.fullname = 'Petr Petrov'
print(emp.fullname)
del emp.fullname
print(emp.fullname)

"""
Первая часть видео, пояснения

class Employee:

    def __init__(self, first, last):
        self.first = first  # приватные атрибуты
        self.last = last  # приватные атрибуты
        self.__email = f'{self.first}.{self.last}@email.com'

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


emp_1 = Employee('Ivan', 'Ivanov')
print(emp_1.get_email())

"""

"""
# Задачи практики
"""

"""
# 1я часть собираем через методы
class Employee:

    def __init__(self, first, last):
        self.first = first  # приватные атрибуты
        self.last = last  # приватные атрибуты

    def email(self):
        return f'{self.first}.{self.last}@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp = Employee('Ivan', 'Ivanov')
print(emp.email())
print(emp.fullname())


"""


"""
# обратиться к атрибуту без скобочек можно, если мы задали атрибут через property
# реализовали getter, setter, deleter


class Employee:

    def __init__(self, first, last):
        self.first = first  # приватные атрибуты
        self.last = last  # приватные атрибуты

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, new_fullname):
        first, last = new_fullname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'delete fullname - {self.fullname}')
        self.first = None
        self.last = None



emp = Employee('Ivan', 'Ivanov')
print(emp.email)  # вывод без круглых скобок
print(emp.fullname)  # вывод без круглых скобок

emp.fullname = 'Petr Petrov'
print(emp.fullname)
del emp.fullname
print(emp.fullname)
"""