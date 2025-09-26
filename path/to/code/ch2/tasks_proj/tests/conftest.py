import pytest
import tasks

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Start and stop a tasks DB for testing."""
    # tmpdir is a temporary directory pytest provides
    tasks.start_tasks_db(str(tmpdir), 'tiny')   # initialize db
    yield
    tasks.stop_tasks_db()  