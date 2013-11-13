"""
Test list1 with pytest

To run tests : py.test             test_list1.py
          or : python -m pytest    test_list1.py
Verobse (-v) : py.test -v          test_list1.py
          or : python -m pytest -v test_list1.py
"""

from list1 import *


def test_first_last6():
    assert first_last6([1, 2, 6]) == True
    assert first_last6([6, 1, 2, 3]) == True
    assert first_last6([13, 6, 1, 2, 3]) == False


def test_same_first_last():
    assert same_first_last([1, 2, 3]) == False
    assert same_first_last([1, 2, 3, 1]) == True
    assert same_first_last([1, 2, 1]) == True


def test_make_pi():
    assert make_pi() == [3, 1, 4]


def test_common_end():
    assert common_end([1, 2, 3], [7, 3]) == True
    assert common_end([1, 2, 3], [7, 3, 2]) == False
    assert common_end([1, 2, 3], [1, 3]) == True


def test_sum3():
    assert sum3([1, 2, 3]) == 6
    assert sum3([5, 11, 2]) == 18
    assert sum3([7, 0, 0]) == 7


def test_rotate_left3():
    assert rotate_left3([1, 2, 3]) == [2, 3, 1]
    assert rotate_left3([5, 11, 9])== [11, 9, 5]
    assert rotate_left3([7, 0, 0]) == [0, 0, 7]


def test_reverse3():
    assert reverse3([1, 2, 3]) == [3, 2, 1]
    assert reverse3([5, 11, 9]) == [9, 11, 5]
    assert reverse3([7, 0, 0]) == [0, 0, 7]


def test_max_end3():
    assert max_end3([1, 2, 3]) == [3, 3, 3]
    assert max_end3([11, 5, 9]) == [11, 11, 11]
    assert max_end3([2, 11, 3]) == [3, 3, 3]


def test_sum2():
    assert sum2([1, 2, 3]) == 3
    assert sum2([1, 1]) == 2
    assert sum2([1, 1, 1, 1]) == 2


def test_middle_way():
    assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
    assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
    assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]


def test_make_ends():
    assert make_ends([1, 2, 3]) == [1, 3]
    assert make_ends([1, 2, 3, 4]) == [1, 4]
    assert make_ends([7, 4, 6, 2]) == [7, 2]


def test_has23():
    assert has23([2, 5]) == True
    assert has23([4, 3]) == True
    assert has23([4, 5]) == False
