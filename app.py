import unicodedata

tasks = []


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    if any(0xD800 <= ord(c) <= 0xDFFF for c in task):
        print("Error: Task contains invalid characters.")
        return False

    cleaned_task = task.strip()

    start = 0
    end = len(cleaned_task)

    while start < end and unicodedata.category(cleaned_task[start]) == "Cf":
        start += 1

    while end > start and unicodedata.category(cleaned_task[end - 1]) == "Cf":
        end -= 1

    cleaned_task = cleaned_task[start:end].strip()

    if not cleaned_task:
        print("Error: Task cannot be empty.")
        return False

    if any(
        unicodedata.category(c) in ("Cc", "Zl", "Zp")
        for c in cleaned_task
    ):
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
    
