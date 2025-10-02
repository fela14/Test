import pytest
import tasks

class TestUpdate:
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update({'dict instead': 1}, tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


#===========================================================#

def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add('not a Task object')


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')

    # Now check the actual message after the block
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
