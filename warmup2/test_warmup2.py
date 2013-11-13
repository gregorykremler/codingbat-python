"""
Test warmup2 with pytest

To run tests : py.test             test_warmup2.py
          or : python -m pytest    test_warmup2.py
Verobse (-v) : py.test -v          test_warmup2.py
          or : python -m pytest -v test_warmup2.py
"""

from warmup2 import *


def test_string_times():
    assert string_times('Hi', 2) == 'HiHi'
    assert string_times('Hi', 3) == 'HiHiHi'
    assert string_times('Hi', 1) == 'Hi'

def test_front_times():
    assert front_times('Chocolate', 2) == 'ChoCho'
    assert front_times('Chocolate', 3) == 'ChoChoCho'
    assert front_times('Abc', 3) == 'AbcAbcAbc'



def test_string_bits():
    assert string_bits('Hello') == 'Hlo'
    assert string_bits('Hi') == 'H'
    assert string_bits('Heeololeo') == 'Hello'


def test_string_splosion():
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'


def test_last2():
    assert last2('hixxhi') == 1
    assert last2('xaxxaxaxx') == 1
    assert last2('axxxaaxx') == 2


def test_array_count9():
    assert array_count9([1, 2, 9]) == 1
    assert array_count9([1, 9, 9]) == 2
    assert array_count9([1, 9, 9, 3, 9]) == 3


def test_array_front9():
    assert array_front9([1, 2, 9, 3, 4]) == True
    assert array_front9([1, 2, 3, 4, 9]) == False
    assert array_front9([1, 2, 3, 4, 5]) == False


def test_array123():
   assert array123([1, 1, 2, 3, 1]) == True
   assert array123([1, 1, 2, 4, 1]) == False
   assert array123([1, 1, 2, 1, 2, 3]) == True


def test_string_match():
   assert string_match('xxcaazz', 'xxbaaz') == 3
   assert string_match('abc', 'abc') == 2
   assert string_match('abc', 'axc') == 0
