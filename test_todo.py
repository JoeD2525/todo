from todo import add_task, list_tasks, done_task
import pytest

def test_add_task():
    assert add_task([], "buy milk") == [{"title": "buy milk", "done": False}]

def test_list_tasks():
    tasks = [{"title": "buy milk", "done": False}]
    assert list_tasks(tasks) == ["1. [ ] buy milk"]

def test_list_tasks_done():
    tasks = [{"title": "a", "done": True}, {"title": "b", "done": False}]
    assert list_tasks(tasks) == ["1. [x] a", "2. [ ] b"]

def test_done_task():
    tasks = [{"title": "buy milk", "done": False}]
    assert done_task(tasks, 1) == [{"title": "buy milk", "done": True}]

def test_done_task_bad_number():
    with pytest.raises(ValueError):
        done_task([{"title": "a", "done": False}],5)

def test_done_task_zero():
    with pytest.raises(ValueError):
        done_task([{"title": "a", "done": False}],0)

def test_list_tasks_empty():
    assert list_tasks([]) == []



    #why pass [] along with buy milk