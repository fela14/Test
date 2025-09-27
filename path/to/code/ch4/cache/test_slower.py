import datetime
import pytest
import time
import random

@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # nodeid = unique pytest test identifier (can contain colons)
    # since cache keys become filenames in .pytest_cache,
    # colons are replaced with underscores for safety

    start_time = datetime.datetime.now()
    yield   # <-- let the test run
    stop_time = datetime.datetime.now()

    this_duration = (stop_time - start_time).total_seconds()

    last_duration = cache.get(key, None)
    cache.set(key, this_duration)   # store this run’s duration

    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring

@pytest.mark.parametrize("i", range(5))
def test_slow_stuff(i):
    time.sleep(random.random())  # sleep between 0.0 and 1.0 seconds

