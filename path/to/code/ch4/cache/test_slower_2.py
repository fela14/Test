import datetime
import pytest
from collections import namedtuple

# Named tuple to keep both current and last run durations
Duration = namedtuple('Duration', ['current', 'last'])

@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'
    # current = {}, last = durations from previous run (if any)
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    # after all tests, store current durations for next run
    request.config.cache.set(key, d.current)

@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield  # run the test
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration  # store this run’s duration

    if d.last.get(nodeid, None) is not None:
        errorstring = "test duration over 2x last duration"
        assert duration <= (d.last[nodeid] * 2), errorstring


# Example test (slow-ish, randomized duration)
import time, random

@pytest.mark.parametrize("i", range(5))
def test_slow_stuff(i):
    time.sleep(random.random())  # simulate some variable runtime
