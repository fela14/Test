import pytest
import tasks

@pytest.fixture(autouse=True)
def tasks_db(tmpdir):
    """Connect to a temporary tasks DB before tests, disconnect after."""
    # Setup: start the tasks database in a temporary folder
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # <-- test code runs here

    # Teardown: stop the tasks database after the test
    tasks.stop_tasks_db()
