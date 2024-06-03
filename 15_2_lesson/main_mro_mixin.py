class Employee:

    def __init__(self):
        self.pay = self.id * 10000
        super().__init__()


class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1
        self.order_log()
        super().__init__()

    def order_log(self):
        print(f'{self.id}-й сотрудник')


class Developer(Employee, MixinLog):

    def __init__(self):
        super().__init__()

    def work(self):
        print('Write some code')

    def code(self):
        pass


dev1 = Developer('Ivan', 'Ivanov')
dev1.order_log()

dev2 = Developer('Elena', 'Ivanova')
dev2.order_log()