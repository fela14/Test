# ch7/unittest/test_delete_unittest.py
import unittest
import tasks
from tasks import Task
import pytest

@pytest.mark.usefixtures("tasks_db_session")  # ensures DB is set up for each test
class TestNonEmpty(unittest.TestCase):

    def setUp(self):
        tasks.delete_all()  # start empty
        # add 3 tasks
        self.ids = []
        self.ids.append(tasks.add(Task('One', 'Brian', True)))
        self.ids.append(tasks.add(Task('Two', 'Still Brian', False)))
        self.ids.append(tasks.add(Task('Three', 'Not Brian', False)))

    def test_delete_decreases_count(self):
        # GIVEN 3 items
        self.assertEqual(tasks.count(), 3)
        # WHEN we delete one
        tasks.delete(self.ids[0])
        # THEN count decreases by 1
        self.assertEqual(tasks.count(), 2)
