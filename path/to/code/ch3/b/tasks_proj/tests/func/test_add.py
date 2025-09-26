# test_add.py

import pytest
import tasks
from tasks import Task

# Apply fixtures just for setup/teardown (no need as function args)
@pytest.mark.usefixtures("tasks_db", "tasks_just_a_few")
class TestAdd:

    def test_add_task(self):
        """Add a new task to an empty DB."""
        task_id = tasks.add(Task('do nothing'))
        # tasks_db is empty at start, so only 1 task exists
        assert tasks.count() == 1
