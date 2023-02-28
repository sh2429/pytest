import pytest
import math

@pytest.mark.square
def test_sqrt():             # test will be passed successfull
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsqr():             # test will be failed
    num = 7
    assert 7 * 7 == 40

@pytest.mark.others
def test_equality():   
    assert 10 == 11

