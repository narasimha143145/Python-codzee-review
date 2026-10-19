
"""
TaskFlow: Task Management System
A medium-level Python project demonstrating
validation, CRUD operations, filtering, and error handling.
"""

from datetime import datetime, timezone
from uuid import uuid4


class Task:
    """Represent an individual task."""

    def _init_(self, title, description="", priority="medium"):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        if len(title.strip()) > 100:
            raise ValueError("Task title cannot exceed 100 characters.")

        if priority not in ("low", "medium", "high"):
            raise ValueError("Priority must be low, medium, or high.")

        self.id = str(uuid4())
        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        """Return task details as a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
        }


class TaskManager:
    """Manage task creation, updates, and filtering."""

    def _init_(self):
        self.tasks = {}

    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks[task.id] = task
        return task.to_dict()

    def list_tasks(self, completed=None, priority=None):
        results = list(self.tasks.values())

        if completed is not None:
            results = [
                task for task in results
                if task.completed == completed
            ]

        if priority is not None:
            results = [
                task for task in results
                if task.priority == priority
            ]

        return [task.to_dict() for task in results]

    def complete_task(self, task_id):
        task = self.tasks.get(task_id)

        if task is None:
            raise KeyError("Task not found.")

        task.completed = True
        return task.to_dict()

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found.")

        del self.tasks[task_id]
        return {"message": "Task deleted successfully."}


if _name_ == "_main_":
    manager = TaskManager()

    first = manager.add_task(
        "Prepare project",
        "Create a clean Python project",
        "high",
    )

    manager.add_task(
        "Write documentation",
        "Explain project features",
        "medium",
    )

    manager.complete_task(first["id"])

    print("All tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nPending high-priority tasks:")
    for task in manager.list_tasks(completed=False, priority="high"):
        print(task)
2:26 PM
Hgh
2:31 PM
"""
TaskFlow: Task Management System
A medium-level Python project demonstrating
validation, CRUD operations, filtering, and error handling.
"""

from datetime import datetime, timezone
from uuid import uuid4


class Task:
    """Represent an individual task."""

    def _init_(self, title, description="", priority="medium"):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")

        if len(title.strip()) > 100:
            raise ValueError("Task title cannot exceed 100 characters.")

        if priority not in ("low", "medium", "high"):
            raise ValueError("Priority must be low, medium, or high.")

        self.id = str(uuid4())
        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        """Return task details as a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at,
        }


class TaskManager:
    """Manage task creation, updates, and filtering."""

    def _init_(self):
        self.tasks = {}

    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks[task.id] = task
        return task.to_dict()

    def list_tasks(self, completed=None, priority=None):
        results = list(self.tasks.values())

        if completed is not None:
            results = [
                task for task in results
                if task.completed == completed
            ]

        if priority is not None:
            results = [
                task for task in results
                if task.priority == priority
            ]

        return [task.to_dict() for task in results]

    def complete_task(self, task_id):
        task = self.tasks.get(task_id)

        if task is None:
            raise KeyError("Task not found.")

        task.completed = True
        return task.to_dict()

    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found.")

        del self.tasks[task_id]
        return {"message": "Task deleted successfully."}


if _name_ == "_main_":
    manager = TaskManager()

    first = manager.add_task(
        "Prepare project",
        "Create a clean Python project",
        "high",
    )

    manager.add_task(
        "Write documentation",
        "Explain project features",
        "medium",
    )

    manager.complete_task(first["id"])

    print("All tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nPending high-priority tasks:")
    for task in manager.list_tasks(completed=False, priority="high"):
        print(task)
