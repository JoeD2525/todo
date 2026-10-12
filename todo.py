def add_task(tasks, title):
    return tasks + [{"title": title, "done": False}]

def list_tasks(tasks):
    lines = []
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{number}. [{mark}] {task['title']}")
    return lines