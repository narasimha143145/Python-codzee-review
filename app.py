tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def show_tasks():
    print("My Tasks:")
    for task in tasks:
        print("-", task)

add_task("Learn Python")
add_task("Complete Codzee task")
show_tasks()
