"""Demonstrate -lf and -ff with failing tests."""
import pytest
from pytest import approx

# --- First test set: floating point sums ---
testdata = [
    (1.01, 2.01, 3.02),
    (1e25, 1e23, 1.1e25),
    (1.23, 3.21, 4.44),
    (0.1, 0.2, 0.3),
    (1e25, 1e24, 1.1e25),
]

@pytest.mark.parametrize("x,y,expected", testdata)
def test_sum(x, y, expected):   # renamed from test_a
    """Demo approx() with addition."""
    sum_ = x + y
    assert sum_ == approx(expected)

# --- Second test set: multiplication ---
test_times = [
    (1, 5, 5),
    (8.9, 5, 23.6),
    (2.0, 5, 10.0),
    (5.6, 5, 46.9),
]

@pytest.mark.parametrize("x,y,exp", test_times)
def test_times_calc(x, y, exp):   # renamed from test_a
    """Demo approx() with multiplication."""
    times_ = x * y
    assert times_ == approx(exp)
