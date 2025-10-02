import pytest

@pytest.mark.xfail
def test_broken_feature():
    assert 1 == 2
