import warnings
import pytest

def lame_function():
    warnings.warn('Please stop using this', DeprecationWarning)

def test_lame_function(recwarn):
    # Call the function that issues the warning
    lame_function()

    # There should be exactly one warning recorded
    assert len(recwarn) == 1

    # Retrieve the warning
    w = recwarn.pop()

    # Check the message and category
    assert str(w.message) == 'Please stop using this'
    assert w.category == DeprecationWarning


import warnings
import pytest

def lame_function():
    warnings.warn('Please stop using this', DeprecationWarning)

def test_lame_function_warns():
    # Use pytest.warns as a context manager
    with pytest.warns(DeprecationWarning) as record:
        lame_function()

    # Ensure exactly one warning was raised
    assert len(record) == 1

    # Check the warning message
    assert str(record[0].message) == 'Please stop using this'
