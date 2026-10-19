
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

    # Reject lone surrogate characters before storing or printing.
    if any(0xD800 <= ord(char) <= 0xDFFF for char in task):
        print("Error: Task contains invalid characters.")
        return False

    # Remove ordinary whitespace and known invisible edge characters.
    cleaned_task = task.strip().strip(INVISIBLE_EDGE_CHARS).strip()

    if not cleaned_task:
        print("Error: Task cannot be empty.")
        return False

    # Reject control characters and line or paragraph separators.
    if any(
        unicodedata.category(char) in ("Cc", "Zl", "Zp")
        for char in cleaned_task
    ):
        print("Error: Task cannot contain control characters.")
        return False

    # Reject characters that can look like an empty task.
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
    
