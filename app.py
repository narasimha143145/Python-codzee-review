
import unicodedata

tasks = []

INVISIBLE_EDGE_CHARS = (
    "\u200b\u200e\u200f\u2060\ufeff\u00ad"
    "\u202a\u202b\u202c\u202d\u202e"
)


def clean_task_title(title):
    start = 0
    end = len(title)

    while start < end and (
        title[start].isspace()
        or title[start] in INVISIBLE_EDGE_CHARS
    ):
        start += 1

    while start < end and (
        title[end - 1].isspace()
        or title[end - 1] in INVISIBLE_EDGE_CHARS
    ):
        end -= 1

    return title[start:end]


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    if any(0xD800 <= ord(char) <= 0xDFFF for char in task):
        print("Error: Task contains invalid characters.")
        return False

    cleaned_task = clean_task_title(task)

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
        "completed": False,
        "priority": "medium",
    })

    print(f"Task added: {cleaned_task}")
    return True


def complete_task(task_title):
    if not isinstance(task_title, str):
        print("Error: Task title must be text.")
        return False

    if any(0xD800 <= ord(char) <= 0xDFFF for char in task_title):
        print("Error: Task title contains invalid characters.")
        return False

    normalized_title = clean_task_title(task_title).casefold()

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
        priority = task.get("priority", "medium").capitalize()

        print(
            f"{index}. {task['title']} "
            f"({status}, Priority: {priority})"
        )


def get_task_summary():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
    }


def show_task_summary():
    summary = get_task_summary()
    print(f"Total tasks: {summary['total']}")
    print(f"Completed tasks: {summary['completed']}")
    print(f"Pending tasks: {summary['pending']}")


def set_task_priority(task_title, priority):
    """Set priority on the first pending match, or first match if all completed."""

    if not isinstance(task_title, str):
        print("Error: Task title must be text.")
        return False

    if any(0xD800 <= ord(char) <= 0xDFFF for char in task_title):
        print("Error: Task title contains invalid characters.")
        return False

    if not isinstance(priority, str):
        print("Error: Priority must be low, medium, or high.")
        return False

    normalized_title = clean_task_title(task_title).casefold()
    normalized_priority = priority.strip().lower()

    if not normalized_title:
        print("Error: Task title cannot be empty.")
        return False

    if normalized_priority not in ("low", "medium", "high"):
        print("Error: Priority must be low, medium, or high.")
        return False

    matching_tasks = [
        task for task in tasks
        if task["title"].casefold() == normalized_title
    ]

    if not matching_tasks:
        print("Error: No task found with that title.")
        return False

    target = next(
        (task for task in matching_tasks if not task["completed"]),
        matching_tasks[0],
    )

    target["priority"] = normalized_priority
    print(
        f"Priority updated: {target['title']} "
        f"({normalized_priority})"
    )
    return True


def get_tasks_by_priority(priority):
    """Return copies of tasks matching the requested priority."""

    if not isinstance(priority, str):
        print("Error: Priority must be low, medium, or high.")
        return []

    normalized_priority = priority.strip().lower()

    if normalized_priority not in ("low", "medium", "high"):
        print("Error: Priority must be low, medium, or high.")
        return []

    return [
        task.copy()
        for task in tasks
        if task.get("priority", "medium") == normalized_priority
    ]


if __name__ == "__main__":
    add_task("Complete Codzee task")
    add_task("Review pull requests")
    add_task("Complete Codzee task")

    complete_task("Complete Codzee task")
    set_task_priority("Review pull requests", "high")

    show_tasks()
    show_task_summary()
    
    
