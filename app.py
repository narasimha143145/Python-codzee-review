
tasks = []

INVISIBLE_EDGE_CHARS = "\u200b\u2060\ufeff"


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    cleaned_task = task.strip().strip(INVISIBLE_EDGE_CHARS).strip()

    if not cleaned_task or not any(
        c.isprintable() and not c.isspace()
        for c in cleaned_task
    ):
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
    

