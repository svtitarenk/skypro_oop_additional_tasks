"""
Для магического метода __add__ класса
Employee добавить обработку исключений
при передаче в метод значений, который должны
быть объектами этого же класса или числом.
Написать тесты на обработку исключений.

Чтобы нельзя было прибавить строку, словарь и пр.

flow
Восстановить класс Employee
Написать проверку значений и возбуждать исключение
Написать тесты на обработку возникающих исключений

"""
import pytest


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        elif isinstance(other, (int, float)):
            return self.pay + other
        raise TypeError  # тут критическая ошибка и программа остановится


if __name__ == "__main__":
    emp_1 = Employee('Ivan', 'Ivanov', 50000)
    emp_2 = Employee('Petr', 'Petrov', 50000)

    print(emp_1 + emp_2)
    print(emp_1 + 10000)
    # print(emp_1 + '123124')


    def test_raises():
        emp_3 = Employee('Ivan', 'Ivanov', 50000)

        # оборачиваем код, в котором могут быть исключения
        with pytest.raises(TypeError) as e_info:
            emp_3 + '50000'


    def test_raises_with_dict():
        emp_3 = Employee('Ivan', 'Ivanov', 50000)

        # оборачиваем код, в котором могут быть исключения
        with pytest.raises(TypeError) as e_info:
            emp_3 + {'1': '2'}
