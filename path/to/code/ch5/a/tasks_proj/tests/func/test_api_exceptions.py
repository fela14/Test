import pytest
import tasks
from tasks import Task

# This fixture (tasks_db) is applied to all tests in this class
@pytest.mark.usefixtures('tasks_db')
class TestAdd:
    """Tests related to tasks.add()."""

    def test_missing_summary(self):
        """Should raise an exception if summary is missing."""
        # Expect ValueError when summary is not provided
        with pytest.raises(ValueError):
            tasks.add(Task(owner='bob'))

    def test_done_not_bool(self):
        """Should raise an exception if 'done' is not a boolean."""
        # Expect ValueError when 'done' is not True/False
        with pytest.raises(ValueError):
            tasks.add(Task(summary='do something', done='False'))