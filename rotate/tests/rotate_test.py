"""Run test using pytest."""


import os
import sys


up = os.path.dirname
sys.path.append(up(up(up(os.path.abspath(__file__)))))

# Only in this order
from rotate import reading, ciphers


def test1():
    assert reading.from_string('Original text') == 'Original text'


def test2():
    assert reading.from_string('AbcdE', alg=ciphers.caesar_1) == 'BcdeF'


def test3():
    assert reading.from_string('reebe', alg=ciphers.rot_13) == 'error'


def test4():
    assert ciphers.rot_13('Q') == 'D'


def test5():
    assert ciphers.caesar_1('z') == 'a'
