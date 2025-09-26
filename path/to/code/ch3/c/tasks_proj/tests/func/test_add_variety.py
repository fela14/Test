import pytest
import tasks
from tasks import Task

# ------------------------
# Task data to try
# ------------------------
tasks_to_try = (
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)
)

# Optional: human-readable IDs
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]

# ------------------------
# Equivalence helper
# ------------------------
def equivalent(t1, t2):
    """Check two tasks for equivalence, ignoring ID."""
    return (
        t1.summary == t2.summary and
        t1.owner == t2.owner and
        t1.done == t2.done
    )

# ------------------------
# Parametrized fixtures
# ------------------------
@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Fixture providing one Task object at a time (default IDs)."""
    return request.param

@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Fixture providing one Task with human-readable IDs."""
    return request.param

def id_func(fixture_value):
    """Generate dynamic IDs for parametrized fixture."""
    t = fixture_value
    return 'Task {},{},{}'.format(t.summary, t.owner, t.done)

@pytest.fixture(params=tasks_to_try, ids=id_func)
def c_task(request):
    """Fixture providing one Task at a time with dynamic IDs."""
    return request.param

# ------------------------
# Tests using fixtures
# ------------------------
def test_add_a(tasks_db, a_task):
    """Add tasks using fixture with default IDs."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)

def test_add_b(tasks_db, b_task):
    """Add tasks using fixture with human-readable IDs."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)

def test_add_c(tasks_db, c_task):
    """Add tasks using fixture with dynamic function-generated IDs."""
    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)
