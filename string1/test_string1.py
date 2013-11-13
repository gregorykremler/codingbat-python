"""
Test string1 with pytest

To run tests : py.test             test_string1.py
          or : python -m pytest    test_string1.py
Verobse (-v) : py.test -v          test_string1.py
          or : python -m pytest -v test_string1.py
"""

from string1 import *


def test_hello_name():
    assert hello_name('Bob') == 'Hello Bob!'
    assert hello_name('Alice') == 'Hello Alice!'
    assert hello_name('X') == 'Hello X!'


def test_make_abba():
    assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
    assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
    assert make_abba('What', 'Up') == 'WhatUpUpWhat'


def test_make_tags():
    assert make_tags('i', 'Yay') == '<i>Yay</i>'
    assert make_tags('i', 'Hello') == '<i>Hello</i>'
    assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'


def test_make_out_word():
    assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
    assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
    assert make_out_word('[[]]', 'word') == '[[word]]'


def test_extra_end():
    assert extra_end('Hello') == 'lololo'
    assert extra_end('ab') == 'ababab'
    assert extra_end('Hi') == 'HiHiHi'


def test_first_two():
    assert first_two('Hello') == 'He'
    assert first_two('abcdefg') == 'ab'
    assert first_two('ab') == 'ab'


def test_first_half():
    assert first_half('WooHoo') == 'Woo'
    assert first_half('HelloThere') == 'Hello'
    assert first_half('abcdef') == 'abc'


def test_without_end():
    assert without_end('Hello') == 'ell'
    assert without_end('java') == 'av'
    assert without_end('coding')== 'odin'


def test_combo_string():
    assert combo_string('Hello', 'hi') == 'hiHellohi'
    assert combo_string('hi', 'Hello') == 'hiHellohi'
    assert combo_string('aaa', 'b') == 'baaab'


def test_non_start():
    assert non_start('Hello', 'There') == 'ellohere'
    assert non_start('java', 'code') == 'avaode'
    assert non_start('shotl', 'java') == 'hotlava'


def test_left2():
    assert left2('Hello') == 'lloHe'
    assert left2('java') == 'vaja'
    assert left2('Hi') == 'Hi'
