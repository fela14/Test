import pytest
import time

# -------------------------
# Session-scoped footer
# -------------------------
@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of the entire pytest session."""
    yield  # all tests run here
    now = time.time()
    print("\n--")
    print("finished : {}".format(time.strftime('%d %b %X', time.localtime(now))))
    print("-----------------")

# -------------------------
# Function-scoped footer
# -------------------------
@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report duration of each test function."""
    start = time.time()
    yield  # test runs here
    stop = time.time()
    delta = stop - start
    print("\ntest duration : {:0.3f} seconds".format(delta))

# -------------------------
# Example tests
# -------------------------
def test_1():
    """Simulate a long-ish test."""
    time.sleep(1)

def test_2():
    """Simulate a slightly longer test."""
    time.sleep(1.23)
