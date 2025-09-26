import pytest
import tasks
from tasks import Task


# ----------------------------------------------------------------------
# Fixture to set up and tear down the tasks database automatically
# ----------------------------------------------------------------------
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


# ----------------------------------------------------------------------
# Helper function to compare Task objects (ignores id field)
# ----------------------------------------------------------------------
def equivalent(t1, t2):
    """Check two tasks for equivalence, ignoring id."""
    return (
        t1.summary == t2.summary
        and t1.owner == t2.owner
        and t1.done == t2.done
    )


# ----------------------------------------------------------------------
# 1. Single test case
# ----------------------------------------------------------------------
def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but the id should be the same
    assert equivalent(t_from_db, task)


# ----------------------------------------------------------------------
# 2. Parametrize with list of Task objects
# ----------------------------------------------------------------------
@pytest.mark.parametrize('task', [
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIan', False),
])
def test_add_2(task):
    """tasks.get() using id returned from add() works with multiple tasks."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)


# ----------------------------------------------------------------------
# 3. Parametrize with multiple parameters
# ----------------------------------------------------------------------
@pytest.mark.parametrize('summary, owner, done', [
    ('sleep', None, False),
    ('wake', 'brian', False),
    ('breathe', 'BRIAN', True),
    ('eat eggs', 'BrIaN', False),
])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)   # Build the Task with parameters
    task_id = tasks.add(task)           # Add to DB
    t_from_db = tasks.get(task_id)      # Fetch back
    assert equivalent(t_from_db, task)  # Compare (ignores id)


# ----------------------------------------------------------------------
# 4. Parametrize with predefined list
# ----------------------------------------------------------------------
task_to_try = [
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('wake', 'BRIAN'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False),
]


@pytest.mark.parametrize('task', task_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# ----------------------------------------------------------------------
# 5. Parametrize with custom ids
# ----------------------------------------------------------------------
task_ids = [
    'Task({},{},{})'.format(t.summary, t.owner, t.done)
    for t in task_to_try
]


@pytest.mark.parametrize('task', task_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# ----------------------------------------------------------------------
# 6. Parametrize a whole test class
# ----------------------------------------------------------------------
@pytest.mark.parametrize('task', task_to_try, ids=task_ids)
class TestAdd:
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test, just within a class."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        """We can use the same data for multiple tests."""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id


# ----------------------------------------------------------------------
# 7. Parametrize with pytest.param and explicit ids
# ----------------------------------------------------------------------
@pytest.mark.parametrize('task', [
    pytest.param(Task('create'), id='just summary'),
    pytest.param(Task('inspire', 'joanna'), id='summary/owner'),
    pytest.param(Task('encourage', 'michelle', True), id='summary/owner/done'),
])
def test_add_6(task):
    """Demonstrate pytest.param and id."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
