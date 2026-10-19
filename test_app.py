
import unittest

from app import add_task, tasks


class TestAddTask(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_adds_valid_task(self):
        self.assertIs(add_task("Complete project"), True)
        self.assertEqual(tasks, ["Complete project"])

    def test_normalizes_valid_task(self):
        self.assertIs(add_task("  Complete project  "), True)
        self.assertEqual(tasks, ["Complete project"])

    def test_rejects_invalid_inputs(self):
        invalid_inputs = [
            None,
            123,
            [],
            "",
            "   ",
            "\u200b",
            "\ufeff",
            "\u2060",
            "\u200d",
            "\u200c",
            "\u00ad",
            "\x00",
            " \u200b \ufeff ",
        ]

        for value in invalid_inputs:
            with self.subTest(value=repr(value)):
                tasks.clear()
                self.assertIs(add_task(value), False)
                self.assertEqual(tasks, [])

    def test_strips_invisible_characters_at_edges(self):
        self.assertIs(
            add_task("\u200bComplete project\ufeff"), True
        )
        self.assertEqual(tasks, ["Complete project"])

    def test_preserves_interior_zero_width_character(self):
        self.assertIs(add_task("a\u200bb"), True)
        self.assertEqual(tasks, ["a\u200bb"])

    def test_multiple_valid_tasks(self):
        self.assertIs(add_task("First task"), True)
        self.assertIs(add_task("Second task"), True)
        self.assertEqual(tasks, ["First task", "Second task"])


if __name__ == "__main__":
    unittest.main()
    
