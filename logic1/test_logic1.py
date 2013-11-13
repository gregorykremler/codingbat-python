"""
Test logic1 with pytest

To run tests : py.test             test_logic1.py
          or : python -m pytest    test_logic1.py
Verobse (-v) : py.test -v          test_logic1.py
          or : python -m pytest -v test_logic1.py
"""

from logic1 import *


def test_cigar_party():
    cigar_party(30, False) == False
    cigar_party(50, False) == True
    cigar_party(70, True) == True


def test_date_fashion():
    assert date_fashion(5, 10) == 2
    assert date_fashion(5, 2) == 0
    assert date_fashion(5, 5) == 1


def test_squirell_play():
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True


def test_caught_speeding():
    assert caught_speeding(60, False) == 0
    assert caught_speeding(65, False) == 1
    assert caught_speeding(65, True) == 0


def test_sorta_sum():
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21


def test_alarm_clock():
    assert alarm_clock(1, False) == '7:00'
    assert alarm_clock(5, False) == '7:00'
    assert alarm_clock(0, False) == '10:00'


def test_love6():
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True


def test_in1to10():
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True


def test_near_ten():
    assert near_ten(12) == True
    assert near_ten(17) == False
    assert near_ten(19) == True
