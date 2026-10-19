
import pytest

from app import (
    tasks,
    add_task,
    complete_task,
    clean_task_title,
    get_task_summary,
)


@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()


def test_fixed_point_cleanup_and_completion():
    add_task(" \u200b \u200b x")

    assert tasks[0]["title"] == "x"
    assert tasks[0]["completed"] is False

    assert complete_task("x") is True
    assert tasks[0]["completed"] is True


def test_duplicate_titles_can_all_be_completed():
    add_task("x")
    add_task("x")

    assert complete_task("x") is True
    assert sum(task["completed"] for task in tasks) == 1

    assert complete_task("x") is True
    assert sum(task["completed"] for task in tasks) == 2

    assert complete_task("x") is False


def test_task_summary():
    add_task("First")
    add_task("Second")
    complete_task("First")

    assert get_task_summary() == {
        "total": 2,
        "completed": 1,
        "pending": 1,
    }
    
