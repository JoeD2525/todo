from todo import add_task, list_tasks

def test_add_task():
    assert add_task([], "buy milk") == [{"title": "buy milk", "done": False}]

def test_list_tasks():
    tasks = [{"title": "buy milk", "done": False}]
    assert list_tasks(tasks) == ["1. [ ] buy milk"]

def test_list_tasks_done():
    tasks = [{"title": "a", "done": True}, {"title": "b", "done": False}]
    assert list_tasks(tasks) == ["1. [x] a", "2. [ ] b"]