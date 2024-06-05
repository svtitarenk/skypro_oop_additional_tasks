import pytest

from oop_main.src.task import Task
from oop_main.src.user import User
from oop_main.src.periodic_task import PeriodicTask
from oop_main.src.deadline_task import DeadlineTask


@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.com",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", run_time=60),
            Task("Купить помидоры", "Купить помидоры для салата", run_time=30)
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username="John",
        email="john@mail.com",
        first_name="John",
        last_name="Doe",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата"),
            Task("Купить помидоры", "Купить помидоры для салата"),
            Task("Купить лук", "Купить лук для салата")
        ]
    )


@pytest.fixture
def task():
    return Task("Купить огурцы", "Купить огурцы для салата", created_at='20.05.2024', run_time=60)


@pytest.fixture
def task_with_tuntime1():
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="20.04.2024", run_time=60)


@pytest.fixture
def task_with_tuntime2():
    return Task("Купить перец", "Купить перец для салата", created_at="20.04.2024", run_time=70)


# @pytest.fixture
# def task_iterator(second_user):
#     return TaskIterator(second_user)

@pytest.fixture
def task_periodic1():
    return PeriodicTask("Купить огурцы",
                        "Купить огурцы для салата",
                        '01.04.2024',
                        '01.04.2024',
                        run_time=60,
                        created_at="20.04.2024")


@pytest.fixture
def task_periodic2():
    return PeriodicTask("Купить помидоры",
                        "Купить помидоры для салата",
                        '01.04.2024',
                        '01.04.2024',
                        run_time=60,
                        created_at="20.04.2024")


@pytest.fixture
def task_deadline_task1():
    return DeadlineTask("Купить перец",
                        "Купить перец для салата",
                        '01.04.2024',
                        '01.04.2024',
                        run_time=60,
                        created_at="20.04.2024")


@pytest.fixture
def task_deadline_task2():
    return DeadlineTask("Купить лук",
                        "Купить лук для салата",
                        '01.04.2024',
                        '01.04.2024',
                        run_time=60,
                        created_at="20.04.2024")

@pytest.fixture
def user_without_task():
    return User(
        username="Some",
        email="some@mail.com",
        first_name="Some",
        last_name="User",
    )