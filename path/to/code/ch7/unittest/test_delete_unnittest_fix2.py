# ch7/unittest/test_delete_unittest_fix2.py
import pytest
import unittest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db_non_empty(tasks_db_session, request):
    """Set up DB with 3 tasks and attach ids to the test class."""
    tasks.delete_all()  # start empty
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    ids.append(tasks.add(Task('Two', 'Still Brian', False)))
    ids.append(tasks.add(Task('Three', 'Not Brian', False)))
    request.cls.ids = ids  # attach ids to the test class

@pytest.mark.usefixtures('tasks_db_non_empty')
class TestNonEmpty(unittest.TestCase):

    def test_delete_decreases_count(self):
        # GIVEN 3 items
        self.assertEqual(tasks.count(), 3)
        # WHEN we delete one
        tasks.delete(self.ids[0])
        # THEN count decreases by 1
        self.assertEqual(tasks.count(), 2)
