
import unittest
from app import add_task, tasks


class TestAddTask(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_valid_task(self):
        self.assertTrue(add_task("Learn Python"))
        self.assertEqual(tasks, ["Learn Python"])

    def test_empty_task(self):
        self.assertFalse(add_task("   "))
        self.assertEqual(tasks, [])

    def test_none_task(self):
        self.assertFalse(add_task(None))
        self.assertEqual(tasks, [])

    def test_invisible_task(self):
        self.assertFalse(add_task("\u200b"))
        self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()
  
