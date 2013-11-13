"""
Test list2 with pytest

To run tests : py.test             test_list2.py
          or : python -m pytest    test_list2.py
Verobse (-v) : py.test -v          test_list2.py
          or : python -m pytest -v test_list2.py
"""

from list2 import *


def test_count_evens():
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0


def test_big_diff():
    assert big_diff([10, 3, 5, 6]) == 7
    assert big_diff([7, 2, 10, 9]) == 8
    assert big_diff([2, 10, 7, 2]) == 8


def test_centered_average():
    assert centered_average([1, 2, 3, 4, 100]) == 3
    assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
    assert centered_average([-10, -4, -2, -4, -2, 0]) == -3


def test_sum13():
    assert sum13([1, 2, 2, 1]) == 6
    assert sum13([1, 1]) == 2
    assert sum13([1, 2, 2, 1, 13]) == 6


def test_sum67():
    assert sum67([1, 2, 2]) == 5
    assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
    assert sum67([1, 1, 6, 7, 2]) == 4


def test_has22():
    assert has22([1, 2, 2]) == True
    assert has22([1, 2, 1, 2]) == False
    assert has22([2, 1, 2]) == False
