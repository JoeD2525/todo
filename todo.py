def add_task(tasks, title):
    return tasks + [{"title": title, "done": False}]


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
