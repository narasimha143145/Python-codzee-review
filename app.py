tasks = []

def add_task(task):
  task = task.strip()

  if not task:
     print("Error: Task cannot be empty.")
     return

  tasks.append(task)
  print("Task added:", task)

def show_tasks():
    print("My Tasks:")
    for task in tasks:
        print("-", task)

add_task("Learn Python")
add_task("Complete Codzee task")
add_task("   ")
show_tasks()
