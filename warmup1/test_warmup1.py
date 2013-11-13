"""
Test warmup1 with pytest

To run tests : py.test             test_warmup1.py
          or : python -m pytest    test_warmup1.py
Verobse (-v) : py.test -v          test_warmup1.py
          or : python -m pytest -v test_warmup1.py
"""

from warmup1 import *


def test_sleep_in():
    assert sleep_in(False, False) == True
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True

def test_monkey_trouble():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True
    assert monkey_trouble(True, False) == False

def test_sum_double():
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8

def test_diff21():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0

def test_parrot_trouble():
    assert parrot_trouble(True, 6) == True
    assert parrot_trouble(True, 7) == False
    assert parrot_trouble(False, 6) == False

def test_makes10():
    assert makes10(9, 10) == True
    assert makes10(9, 9) == False
    assert makes10(1, 9) == True

def test_near_hundred():
    assert near_hundred(93) == True
    assert near_hundred(90) == True
    assert near_hundred(89) == False

def test_pos_neg():
    assert pos_neg(1, -1, False) == True
    assert pos_neg(-1, 1, False) == True
    assert pos_neg(-4, -5, True) == True


def test_not_string():
    assert not_string('candy') == 'not candy'
    assert not_string('x') == 'not x'
    assert not_string('not bad') == 'not bad'


def test_missing_char():
    assert missing_char('kitten', 1) == 'ktten'
    assert missing_char('kitten', 0) == 'itten'
    assert missing_char('kitten', 4) == 'kittn'


def test_front_back():
    assert front_back('code') == 'eodc'
    assert front_back('a') == 'a'
    assert front_back('ab') == 'ba'


def test_front3():
    assert front3('Java') == 'JavJavJav'
    assert front3('Chocolate') == 'ChoChoCho'
    assert front3('abc') == 'abcabcabc'
