import os
import json
import tempfile
import io
import sys
import unittest

from Level_2_Intermediate import todo_list_app


class TestTodoListApp(unittest.TestCase):
    def setUp(self):
        # create a temporary file for TODO_FILE and point module to it
        self.tf = tempfile.NamedTemporaryFile(delete=False)
        self.tf.close()
        self.orig_todo = todo_list_app.TODO_FILE
        todo_list_app.TODO_FILE = self.tf.name

    def tearDown(self):
        # restore and remove temp file
        todo_list_app.TODO_FILE = self.orig_todo
        if os.path.exists(self.tf.name):
            os.remove(self.tf.name)

    def read_tasks_file(self):
        with open(todo_list_app.TODO_FILE, 'r') as f:
            return json.load(f)

    def test_add_and_list_tasks(self):
        # add two tasks
        todo_list_app.add_task('Task A')
        todo_list_app.add_task('Task B')
        tasks = self.read_tasks_file()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['task'], 'Task A')
        self.assertFalse(tasks[0]['completed'])

        # capture list output
        buf = io.StringIO()
        old = sys.stdout
        try:
            sys.stdout = buf
            todo_list_app.list_tasks()
        finally:
            sys.stdout = old
        out = buf.getvalue()
        self.assertIn('0. [', out)
        self.assertIn('Task A', out)

    def test_mark_and_delete_tasks(self):
        todo_list_app.add_task('X')
        todo_list_app.add_task('Y')
        # mark first task completed
        todo_list_app.mark_task_completed(0)
        tasks = self.read_tasks_file()
        self.assertTrue(tasks[0]['completed'])

        # delete second task
        todo_list_app.delete_task(1)
        tasks = self.read_tasks_file()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['task'], 'X')

    def test_invalid_delete_and_mark(self):
        # no tasks yet
        buf = io.StringIO()
        old = sys.stdout
        try:
            sys.stdout = buf
            todo_list_app.delete_task(5)
            todo_list_app.mark_task_completed(2)
        finally:
            sys.stdout = old
        out = buf.getvalue()
        self.assertIn('Error: Task index out of range.', out)


if __name__ == '__main__':
    unittest.main()
