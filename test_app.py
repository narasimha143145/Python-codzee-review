
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
            " \u200b \ufeff ",
        ]

        for value in invalid_inputs:
            with self.subTest(value=repr(value)):
                tasks.clear()
                self.assertIs(add_task(value), False)
                self.assertEqual(tasks, [])

    def test_preserves_interior_zero_width_character(self):
        self.assertIs(add_task("a\u200bb"), True)
        self.assertEqual(tasks, ["a\u200bb"])


if __name__ == "__main__":
    unittest.main()
    
