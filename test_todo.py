from todo import add_task

def test_add_task():
    assert add_task([], "buy milk") == [{"title": "buy milk", "done": False}]