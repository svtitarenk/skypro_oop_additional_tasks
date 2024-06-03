import pytest


def test_deadline_task_init(task_deadline_task1):
    assert task_deadline_task1.name == "Купить перец"
    assert task_deadline_task1.description == "Купить перец для салата"
    assert task_deadline_task1.status == "Ожидает старта"
    assert task_deadline_task1.created_at == "20.04.2024"
    assert task_deadline_task1.deadline == "01.04.2024"


def test_deadline_task_add(task_deadline_task1, task_deadline_task2):
    assert task_deadline_task1 + task_deadline_task2 == 120


def test_deadline_task_add_error(task_deadline_task1, task_deadline_task2):
    with pytest.raises(TypeError):
        result = task_deadline_task1 + task_deadline_task2 == 120
