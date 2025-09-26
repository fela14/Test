"""Demo fixture scope."""

import pytest


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""
    print("\n>>> SETUP: session fixture")
    yield
    print("\n<<< TEARDOWN: session fixture")


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""
    print("\n>>> SETUP: function fixture")
    yield
    print("\n<<< TEARDOWN: function fixture")


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""
    print("\n>>> SETUP: module fixture")
    yield
    print("\n<<< TEARDOWN: module fixture")


@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""
    print("\n>>> SETUP: class fixture")
    yield
    print("\n<<< TEARDOWN: class fixture")


def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""


def test_2(sess_scope, mod_scope, func_scope):
    """Demo is more fun with multiple tests."""


@pytest.mark.usefixtures('class_scope')
class TestSomething:
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""

