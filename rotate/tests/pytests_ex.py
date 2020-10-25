"""Tests using pytest.

Report:
    pytest pytests_ex.py -v > pytests_report.txt

"""


import os
import sys

up = os.path.dirname
sys.path.append(up(up(up(os.path.abspath(__file__)))))
this_dir = up(up(up(os.path.abspath(__file__)))) + r'\\Examples\\'

# Only in this order
from rotate import reading, ciphers


def test1():
    assert reading.from_file(this_dir +'ex1.txt',
                             this_dir +'save1.txt', ciphers.rot_13) is None


def test2():
    assert reading.from_file(this_dir +'ex2.txt',
                             this_dir +'save2.txt', ciphers.caesar_1) is None


def test3():
    assert reading.from_file(this_dir+'ex3.txt',
                             this_dir+'save3.txt') is None


def test4():
    assert ciphers.rot_13('Q') == 'D'


def test5():
    assert reading.from_string('reebe', ciphers.rot_13) == 'error'
