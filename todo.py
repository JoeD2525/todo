# title.strip() removes spaces from both ends of the text. "" and " " both become "".
# not "" is True, so an empty or all-space title raises the error.
# A normal title such as "buy milk" skips the if and works as before.
def add_task(tasks, title):
    if not title.strip():
        raise ValueError("Task title cannot be empty")
    return tasks + [{"title": title, "done": False}]


# previous version of add task without check on blank or empty(all space) titl
# def add_task(tasks, title):
#     return tasks + [{"title": title, "done": False}]


def list_tasks(tasks):
    lines = []
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{number}. [{mark}] {task['title']}")
    return lines


def done_task(tasks, number):
    if number < 1 or number > len(tasks):
        raise ValueError(f"No task number {number}")
    new_tasks = [dict(task) for task in tasks]
    new_tasks[number - 1]["done"] = True
    return new_tasks
