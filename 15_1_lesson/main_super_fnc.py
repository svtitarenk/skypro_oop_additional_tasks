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
    #  убираем rais_amt и добавляем метод apply_rais
    raise_amt = 1.1  # Атрибут на уровне класса -> в родительском классе он 1.04

    #  дублирование переопределения атрибутов, поэтому этот ког можно заменить на super() ниже + добавление атрибута prog_lang
    # def __init__(self, first, last, pay, prog_lang):
    #     self.first = first
    #     self.last = last
    #     self.pay = pay

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev1 = Developer('Petr', 'Petrov', 50000, 'python')
print(dev1.first)
print(dev1.last)
print(dev1.pay)
print(dev1.prog_lang)

# emp1 = Employee('Ivan', 'Ivanov', 50000)
# print(emp1.pay)  # 50000
# emp1.apply_raise()
# print(emp1.pay)  # 52000
#
# dev1 = Developer('Petr', 'Petrov', 50000, 'python')
# print(dev1.pay)  # 50000
# dev1.apply_raise()  # применяем метод, потом принт!! метод apply_raise есть только в методе Employee, но наследуется в Developer
# print(dev1.pay)  # 55000


# dev1 = Developer('Petr', 'Petrov', 50000, 'python')
# print(dev1.first)
# print(dev1.last)
# print(dev1.pay)
# print(dev1.apply_raise)
# print(dev1.prog_lang)
# dev1.apply_raise()
# print(dev1.pay)

