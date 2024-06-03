import pytest

from main import Employee


@pytest.fixture()
def employee_ivan():
    return Employee('Ivan', 'Ivanov', 50000)


def test_init(employee_ivan):
    assert employee_ivan.name == "Ivan"
    assert employee_ivan.surname == "Ivanov"
    assert employee_ivan.pay == 50000
    assert employee_ivan.email == "Ivan.Ivanov@email.com"


def test_is_work(employee_ivan):
    assert employee_ivan.is_work is False
    employee_ivan.work()
    assert employee_ivan.is_work is True


def test_is_work_not_vacation(employee_ivan):
    employee_ivan.go_to_vacation()
    employee_ivan.work()
    # assert employee_ivan.is_vacation is False
    assert not employee_ivan.is_vacation

def test_is_vacation(employee_ivan):
    assert not employee_ivan.is_vacation
    employee_ivan.go_to_vacation()
    assert employee_ivan.is_vacation


def test_is_vacation_not_work(employee_ivan):
    employee_ivan.go_to_vacation()
    employee_ivan.work()
    assert not employee_ivan.is_work
