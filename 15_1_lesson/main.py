class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)



class Developer(Employee):
    # pass  # Если поставить заглушку, то класс полностью наследует все методы род.класса
    """ # по условию задачи нужно сделать увеличение на 10% """
    raise_amt = 1.1  # Атрибут на уровне класса -> в родительском классе он 1.04


emp1 = Employee('Ivan', 'Ivanov', 50000)
print(emp1.pay)  # 50000
emp1.apply_raise()
print(emp1.pay)  # 52000

dev1 = Developer('Petr', 'Petrov', 50000)
print(dev1.pay)  # 50000
dev1.apply_raise()  # метод apply_raise есть только в методе Employee, но наследуется в Developer
print(dev1.pay)  # 55000

