import datetime
from oop_main.src.task import Task


def test_task_init(task):
    assert task.name == "Купить огурцы"
    assert task.description == "Купить огурцы для салата"
    assert task.status == "Ожидает старта"
    assert task.created_at == "20.05.2024"


# проверка новой задачи
def test_task_created():
    task = Task("Купить билеты", "Купить билеты на смолёт")
    task.name = "Купить билеты"
    task.description = "Купить Купить билеты на смолёт"
    task.status = "Ожидает старта"
    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')


#  провеврить сеттер
#  обращаемся к capsys для того, чтобы перехватить поток вывода и забрать сообщение
def test_task_update(capsys, task):
    task.created_at = "24.02.2024"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')
    assert task.created_at == '28.05.2024'