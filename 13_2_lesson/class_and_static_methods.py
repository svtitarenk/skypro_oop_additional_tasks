import datetime


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Jon', 'Snow', 50000)
emp_2 = Employee('Ivan', 'Ivanov', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'Jon-Snow-70000'
emp_str_2 = 'Ivan-Ivanov-30000'
emp_str_3 = 'Elena-Nikitina-90000'

first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2023, 1, 31)
print(Employee.is_workday(my_date))

"""
первый класс-метод 

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        

# emp_str_1 = 'Jon-Snow-70000'
# emp_str_2 = 'Ivan-Ivanov-30000'
# emp_str_3 = 'Elena-Nikitina-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

"""

"""
# 15:00 
# cls - обращение к классу
# set_raise_amt -- добавляем и тестируем класс-метод set_raise_amt в нем вводим новое значение 
# и получаем увеличение amt

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt


# для проверки

emp_1 = Employee('Jon', 'Snow', 50000)
emp_2 = Employee('Ivan', 'Ivanov', 60000)

print(Employee.raise_amt)

Employee.set_raise_amt(1.05) # задаем новую ставку повышения amount (amt)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
"""

"""
# staticmethod workday weekday
# проверка, я вляется ли день, выходным днем.

import datetime


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return True

        return False

my_date = datetime.date(2023, 1, 31)
print(Employee.is_workday(my_date))

"""
