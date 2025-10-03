# ch7/unittest/conftest.py
import pytest
import tempfile
import shutil
import tasks
from tasks import Task

@pytest.fixture(scope="function")
def tasks_db_session():
    """Set up a temporary DB for each test and tear it down afterwards."""
    temp_dir = tempfile.mkdtemp()
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield  # tests run here
    tasks.stop_tasks_db()
    shutil.rmtree(temp_dir)

@pytest.fixture
def db_with_3_tasks(tasks_db_session):
    """Create a fresh DB with 3 tasks for each test."""
    tasks.delete_all()
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    ids.append(tasks.add(Task('Two', 'Still Brian', False)))
    ids.append(tasks.add(Task('Three', 'Not Brian', False)))
    return ids
