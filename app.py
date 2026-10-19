
tasks = []

def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    task = task.replace("\u200b", "").replace("\ufeff", "").strip()

    if not task or not any(
        char.isprintable() and not char.isspace()
        for char in task
    ):
        print("Error: Task cannot be empty.")
        return False

    tasks.append(task)
    print("Task added:", task)
    return True

def show_tasks():
    print("My Tasks:")
    for task in tasks:
        print("-", task)

add_task("Learn Python")
add_task("Complete Codzee task")
add_task("   ")
add_task(None)
add_task("\u200b")
show_tasks()

