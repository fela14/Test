import pytest
import unnecessary_math

# This fixture runs automatically for all doctests
@pytest.fixture(autouse=True)
def add_um(doctest_namespace):
    """
    Injects 'um' into the doctest namespace.
    Now all doctests can use `um.multiply` and `um.divide`
    without importing the module inside the docstring.
    """
    doctest_namespace['um'] = unnecessary_math
