import pytest
import datetime
from oop_main.src.task import Task


def test_task_init(first_user, second_user):
    assert first_user.username == "User"
    assert first_user.email == "user@mail.com"
    assert len(first_user.task_in_list) == 2  # 13_2 для приватного атрибута, поменяем task_list на getter task_in_list

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert first_user.all_tasks_count == 5



def test_user_task_list_property(first_user):
    # print(first_user.task_list)  # проверяем через pytest -s (-s нужен для того, чтобы проверить print)
    assert first_user.task_list == ("Купить огурцы, Статус выполнения: Ожидает старта, Дата создания: 06.06.2024\n"
                                    "Купить помидоры, Статус выполнения: Ожидает старта, Дата создания: 06.06.2024\n")


def test_user_task_list_setter(first_user, task):
    print(first_user.task_in_list)
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


def test_user_task_list_setter_error(first_user, task):
    with pytest.raises(TypeError):
        first_user.task_list = 1


def test_user_task_list_setter_periodic_task(first_user, task_periodic1):
    first_user.task_list = task_periodic1
    assert first_user.task_in_list[-1].name == "Купить огурцы"

def test_middle_runtime(first_user, user_without_task):
    assert first_user.middle_task_runtime() == 45
    assert user_without_task.middle_task_runtime() == 0

def test_custom_exception(capsys, first_user):
    assert len(first_user.task_in_list) == 2

    task_add = Task("Купить огурцы", "Купить огурцы для салата", created_at="08.04.2024")
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Нельзя задать задачу с нулевым временем выполнения"
    assert message.out.strip().split('\n')[-1] == "Обработка добавления задачи завершена"
