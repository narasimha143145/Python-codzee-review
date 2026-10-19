
import unittest
from app import add_task, tasks


class TestAddTask(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_valid_task(self):
        self.assertTrue(add_task("Learn Python"))
        self.assertEqual(tasks, ["Learn Python"])

    def test_normalizes_valid_task(self):
        self.assertTrue(add_task("  a\u200bb "))
        self.assertEqual(tasks, ["ab"])

    def test_rejects_invalid_inputs(self):
        invalid_inputs = [
            None, 123, [], "", "   ",
            "\u200b", "\ufeff", " \u200b \ufeff ", "\u2060"
        ]
        for value in invalid_inputs:
            with self.subTest(value=repr(value)):
                tasks.clear()
                self.assertFalse(add_task(value))
                self.assertEqual(tasks, [])

    def test_multiple_valid_tasks(self):
        self.assertTrue(add_task("Task one"))
        self.assertTrue(add_task("Task two"))
        self.assertEqual(tasks, ["Task one", "Task two"])


if __name__ == "__main__":
    unittest.main()
    
