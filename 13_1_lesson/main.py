
class Employee:
    name: str
    surname: str
    email: str
    pay: str

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f"{self.name}.{self.surname}@email.com"
        self.is_work = False
        self.is_vacation = False

    def work(self):
        self.is_work = True
        self.is_vacation = False
        print("do some work")

    def go_to_vacation(self):
        self.is_vacation = True
        self.is_work = False
        print("go to vacation")


if __name__ == '__main__':
    emp1 = Employee('Ivan', 'Ivanov', 50000)


