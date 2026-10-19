
import unicodedata

tasks = []

INVISIBLE_EDGE_CHARS = "\u200b\u200c\u200d\u2060\ufeff\u00ad\u200e\u200f\u202a\u202b\u202c\u202d\u202e"


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    cleaned_task = task.strip()

    while cleaned_task and unicodedata.category(cleaned_task[0]) == "Cf":
        cleaned_task = cleaned_task[1:]

    while cleaned_task and unicodedata.category(cleaned_task[-1]) == "Cf":
        cleaned_task = cleaned_task[:-1]

    cleaned_task = cleaned_task.strip()

    if not cleaned_task:
        print("Error: Task cannot be empty.")
        return False

    if any(unicodedata.category(c) == "Cc" for c in cleaned_task):
        print("Error: Task cannot contain control characters.")
        return False

    visible_chars = [
        c for c in cleaned_task
        if c.isprintable()
        and not c.isspace()
        and c not in ("\u3164", "\u2800")
    ]

    if not visible_chars:
        print("Error: Task cannot be empty.")
        return False

    tasks.append(cleaned_task)
    print(f"Task added: {cleaned_task}")
    return True


def show_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    add_task("Complete Codzee task")
    add_task("   ")
    add_task(None)
    add_task("\u200b")
    show_tasks()
    
