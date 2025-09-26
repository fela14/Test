import pytest
import tasks
from tasks import Task

# ------------------------
# Session-scoped DB setup for multiple DB backends
# ------------------------
@pytest.fixture(scope='session', params=['tiny', 'mongo'])
def tasks_db_session(tmpdir_factory, request):
    """Connect to a DB before tests, disconnect after all tests.

    Runs once per DB type ('tiny' or 'mongo') for the session.
    """
    if request.param == 'mongo':
        pytest.skip("MongoDB tests skipped in Codespaces")
    
    # Create a temporary directory for the database (used for 'tiny')
    temp_dir = tmpdir_factory.mktemp('temp')

    # Start the tasks DB for the current DB type
    tasks.start_tasks_db(str(temp_dir), request.param)

    # Yield control to tests
    yield

    # Teardown: stop the database after tests
    tasks.stop_tasks_db()


# ------------------------
# Function-scoped DB fixture (empty DB for each test)
# ------------------------
@pytest.fixture()
def tasks_db(tasks_db_session):
    """Provide a clean tasks database for each test."""
    tasks.delete_all()
