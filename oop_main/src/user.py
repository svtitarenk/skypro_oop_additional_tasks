from oop_main.src.task import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: str
    users_count = 0  # задаем атирубты именно Класса, а не экземпляра класса
    all_tasks_count = 0  # задаем атирубты именно Класса, а не экземпляра класса

    def __init__(self, username, email, first_name, last_name, task_list=None):  # Знаячение task_list по умолчанию None + обработка в инициализации, если не пустой
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []  #  задаем проверку, если task_list пустой, тогда пустой список
        User.users_count += 1  #  делаем обращение к классу, и потом атрибуту класса
        User.all_tasks_count += len(task_list) if task_list else 0  # увеличиваем на КОЛИЧЕСТВО задач + добавляем проверку, если он пустой, увеличиваем на 0


    # задаем Геттер и сеттер
    @property
    def task_list(self):
        # task_list это список, поэтому его нужно перебрать и включить задачи в task_str
        # обращаемся к нашему импортированному классу from oop_main.src.task import Task
        task_str = ""
        for task in self.__task_list:
            task_str +=  f"{task.name}, Статус выполнения: {task.status}, Дата создания: {task.created_at}\n"

        return task_str

    # Дополнительно реализовать проверку в @task_list.setter, что будут передаваться экземпляры класса Task или его наследников
    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):  # если мы будем указывать и наследников, то проверка будет выполняться корректно
            self.__task_list.append(task)
            User.all_tasks_count += 1
        else:
            raise TypeError

    @property
    def task_in_list(self):
        return self.__task_list


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Купить огурцы для салата")
    task2 = Task("Купить подмидоры", "Купить помидоры для салата")
    task3 = Task("Купить лук", "Купить лук для салата")
    task4 = Task("Купить перец", "Купить перец для салата")

    user = User('User', 'user@email.com', 'User', 'Userov', [task1, task2, task3, task4])
    print('user.username:', user.username)
    print('user.email:', user.email)
    print('user.first_name:', user.first_name)
    print('user.last_name:', user.last_name)
    print('user.task_list:', user.task_list, sep='\n')  # у нас уже есть обращение к атирубуту task

    print('user.users_count:', user.users_count)
    print('User.all_tasks_count', User.all_tasks_count)

    # 13_2 добавляем новую задачу
    task5 = Task("Купить огурцы", "Купить огурцы для салата")
    # Проверка - Дополнительно реализовать проверку в @task_list.setter, что будут передаваться экземпляры класса Task или его наследников
    user.task_list = task5
    print('user.task_list:', user.task_list, sep='\n')
    print('User.all_tasks_count:', User.all_tasks_count)

