"""Tests using pytest.

Report:
    pytest pytests_ex.py -v > pytests_report.txt

"""


from rotate import reading, ciphers
import os


up = os.path.dirname
this_dir = up(up(up(os.path.abspath(__file__)))) + r'\\Examples\\'


def test1():
    assert reading.from_file(this_dir+'ex1.txt', this_dir+'save1.txt', ciphers.rot13) is None


def test2():
    assert reading.from_file(this_dir+'ex2.txt', this_dir+'save2.txt', ciphers.caesar1) is None


def test3():
    assert reading.from_file(this_dir+'ex3.txt', this_dir+'save3.txt') is None


def test4():
    assert ciphers.rot13('Q') == 'D'


def test5():
    assert reading.from_string('reebe', ciphers.rot13) == 'error'
