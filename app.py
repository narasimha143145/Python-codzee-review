
tasks = []

INVISIBLE_EDGE_CHARS = "\u200b\u2060\ufeff"


def add_task(task):
    if not isinstance(task, str):
        print("Error: Task must be text.")
        return False

    # Remove whitespace and invisible characters at the edges only.
    cleaned_task = task.strip().strip(INVISIBLE_EDGE_CHARS).strip()

    if not cleaned_task:
        print("Error: Task cannot be empty.")
        return False

    tasks.append(cleaned_task)
    return True


if __name__ == "__main__":
    add_task("Complete Codzee task")
    add_task("   ")
    add_task(None)
    add_task("\u200b")
    print(tasks)
    

