import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.xfail()
def test_fail():
    assert 3 == 4

