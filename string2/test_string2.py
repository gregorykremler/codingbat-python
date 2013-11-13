"""
Test string2 with pytest

To run tests : py.test             test_string2.py
          or : python -m pytest    test_string2.py
Verobse (-v) : py.test -v          test_string2.py
          or : python -m pytest -v test_string2.py
"""

from string2 import *


def test_double_char():
    assert double_char('The') == 'TThhee'
    assert double_char('AAbb') == 'AAAAbbbb'
    assert double_char('Hi-There') == 'HHii--TThheerree'


def test_count_hi():
    assert count_hi('abc hi ho')== 1
    assert count_hi('ABChi hi') == 2
    assert count_hi('hihi') == 2


def test_cat_dog():
    assert cat_dog('catdog') == True
    assert cat_dog('catcat') == False
    assert cat_dog('1cat1cadodog') == True


def test_count_code():
    assert count_code('aaacodebbb') == 1
    assert count_code('codexxcode') == 2
    assert count_code('cozexxcope') == 2


def test_end_other():
    assert end_other('Hiabc', 'abc') == True
    assert end_other('AbC', 'HiaBc') == True
    assert end_other('abc', 'abXabc') == True


def test_xyz_there():
    assert xyz_there('abcxyz') == True
    assert xyz_there('abc.xyz') == False
    assert xyz_there('xyz.abc') == True
