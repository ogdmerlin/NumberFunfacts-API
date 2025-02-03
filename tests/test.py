# test place holder

import pytest


@pytest.mark.xfail
def test_fails():
    assert False


@pytest.mark.xfail
def test_succeeds():
    assert True
