
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


# add_task validation tests

@pytest.mark.parametrize(
    "value",
    [None, 123, [], {}],
)
def test_add_task_rejects_non_string(value):
    assert add_task(value) is False
    assert tasks == []


@pytest.mark.parametrize(
    "title",
    [
        "",
        " ",
        "   ",
        "\u200b",
        "\ufeff",
        "\u200b\ufeff",
        "\u3164",
        "\u2800",
    ],
)
def test_add_task_rejects_empty_or_invisible_title(title):
    assert add_task(title) is False
    assert tasks == []


@pytest.mark.parametrize(
    "title",
    [
        "\ud800",
        "\udfff",
        "hello\x00world",
        "hello\nworld",
        "hello\u2028world",
        "hello\u2029world",
    ],
)
def test_add_task_rejects_invalid_characters(title):
    assert add_task(title) is False
    assert tasks == []


def test_add_task_trims_whitespace():
    assert add_task("  hello  ") is True
    assert tasks[0]["title"] == "hello"


def test_add_task_rejects_invisible_only_title():
    assert add_task(" \u200b \ufeff ") is False
    assert tasks == []


# clean_task_title edge cases

@pytest.mark.parametrize(
    ("title", "expected"),
    [
        (" \u200b \u200b x", "x"),
        ("x \u200b \u200b ", "x"),
        (" \u200b x \u200b ", "x"),
        ("\ufeffhello\u200b", "hello"),
        ("hello", "hello"),
    ],
)
def test_clean_task_title_edges(title, expected):
    assert clean_task_title(title) == expected


# complete_task tests

@pytest.mark.parametrize(
    "value",
    [None, 123, [], {}],
)
def test_complete_task_rejects_non_string(value):
    assert complete_task(value) is False


@pytest.mark.parametrize(
    "title",
    [
        "",
        " ",
        "\u200b",
        "\ufeff",
        "\ud800",
        "\udfff",
    ],
)
def test_complete_task_rejects_invalid_title(title):
    assert complete_task(title) is False


def test_complete_task_case_insensitive():
    add_task("hello")

    assert complete_task("HELLO") is True
    assert tasks[0]["completed"] is True


def test_complete_task_cleans_lookup_title():
    add_task("x")

    assert complete_task(" \u200b \u200b x") is True
    assert tasks[0]["completed"] is True


def test_complete_task_unknown_title():
    assert complete_task("missing") is False


# Regression test for the reported finding

def test_fixed_point_cleanup_and_completion():
    add_task(" \u200b \u200b x")

    assert tasks[0]["title"] == "x"
    assert tasks[0]["completed"] is False

    assert complete_task("x") is True
    assert tasks[0]["completed"] is True


# Duplicate-title behavior

def test_duplicate_titles_complete_first_pending_task():
    add_task("x")
    add_task("x")

    assert complete_task("x") is True
    assert tasks[0]["completed"] is True
    assert tasks[1]["completed"] is False

    assert complete_task("x") is True
    assert tasks[0]["completed"] is True
    assert tasks[1]["completed"] is True

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
    
