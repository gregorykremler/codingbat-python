"""
Test logic2 with pytest

To run tests : py.test             test_logic2.py
          or : python -m pytest    test_logic2.py
Verobse (-v) : py.test -v          test_logic2.py
          or : python -m pytest -v test_logic2.py
"""

from logic2 import *


def test_make_bricks():
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(3, 1, 9) == False
    assert make_bricks(3, 2, 10) == True


def test_lone_sum():
    assert lone_sum(1, 2, 3) == 6
    assert lone_sum(3, 2, 3) == 2
    assert lone_sum(3, 3, 3) == 0


def test_lucky_sum():
    assert lucky_sum(1, 2, 3) == 6
    assert lucky_sum(1, 2, 13) == 3
    assert lucky_sum(1, 13, 3) == 1


def test_no_teen_sum():
    assert no_teen_sum(1, 2, 3) == 6
    assert no_teen_sum(2, 13, 1) == 3
    assert no_teen_sum(2, 1, 14) == 3


def test_round_sum():
    assert round_sum(16, 17, 18) == 60
    assert round_sum(12, 13, 14) == 30
    assert round_sum(6, 4, 4) == 10


def test_close_far():
    assert close_far(1, 2, 10) == True
    assert close_far(1, 2, 3) == False
    assert close_far(4, 1, 3) == True


def test_make_chocolate():
    assert make_chocolate(4, 1, 9) == 4
    assert make_chocolate(4, 1, 10) == -1
    assert make_chocolate(4, 1, 7) == 2
