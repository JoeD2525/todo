from todo import add_task, list_tasks, done_task

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