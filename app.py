
import unicodedata

tasks = []

INVISIBLE_EDGE_CHARS = (
    "\u200b\u200c\u200d\u2060\ufeff\u00ad"
    "\u200e\u200f\u202a\u202b\u202c\u202d\u202e"
)


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    if any(0xD800 <= ord(char) <= 0xDFFF for char in task):
        print("Error: Task contains invalid characters.")
        return False

    cleaned_task = task.strip().strip(INVISIBLE_EDGE_CHARS).strip()

    if not cleaned_task:
        print("Error: Task cannot be empty.")
        return False

    if any(
        unicodedata.category(char) in ("Cc", "Zl", "Zp")
        for char in cleaned_task
    ):
        print("Error: Task cannot contain control characters.")
        return False

    visible_chars = [
        char
        for char in cleaned_task
        if char.isprintable()
        and not char.isspace()
        and char not in ("\u3164", "\u2800")
    ]

    if not visible_chars:
        print("Error: Task cannot be empty.")
        return False

    tasks.append({
        "title": cleaned_task,
        "completed": False
    })
    print(f"Task added: {cleaned_task}")
    return True


def complete_task(task_title):
    if not isinstance(task_title, str):
        print("Error: Task title must be text.")
        return False

    normalized_title = task_title.strip().casefold()

    if not normalized_title:
        print("Error: Task title cannot be empty.")
        return False

    for task in tasks:
        if (
            task["title"].casefold() == normalized_title
            and not task["completed"]
        ):
            task["completed"] = True
            print(f"Task completed: {task['title']}")
            return True

    print("Error: No pending task found with that title.")
    return False


def show_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {status}")


def get_task_summary():
    total = len(tasks)
    completed = sum(
        1 for task in tasks if task["completed"]
    )
    pending = total - completed

    return {
        "total": total,
        "completed": completed,
        "pending": pending
    }


def show_task_summary():
    summary = get_task_summary()
    print(f"Total tasks: {summary['total']}")
    print(f"Completed tasks: {summary['completed']}")
    print(f"Pending tasks: {summary['pending']}")


if __name__ == "__main__":
    add_task("Complete Codzee task")
    add_task("Review pull requests")
    add_task("Complete Codzee task")

    complete_task("Complete Codzee task")

    show_tasks()
    show_task_summary()
    
