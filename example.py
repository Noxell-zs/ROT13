"""Examples in the form of functions"""


import sys
import os
from rotate import reading, ciphers


this_dir = os.path.dirname(os.path.abspath(__file__)) + r'\\Examples\\'


def exam_1():
    """Encrypt text from 'ex1.txt' to 'save1.txt' by ROT13."""
    reading.from_file(this_dir+'ex1.txt', this_dir+'save1.txt', ciphers.rot13)


def exam_2():
    """Encrypt text from 'ex2.txt' to 'save2.txt' by Caesar."""
    reading.from_file(this_dir+'ex2.txt', this_dir+'save2.txt', ciphers.caesar1)


def exam_3():
    """Copy text from 'ex3.txt' to 'save3.txt'."""
    reading.from_file(this_dir+'ex3.txt', this_dir+'save3.txt')


def exam_4():
    """Print the character 'D'."""
    print(ciphers.rot13('Q'))


def exam_5():
    """Print 'error' in the error output."""
    print(reading.from_string('ReEbE', ciphers.rot13), file=sys.stderr)


if __name__ == '__main__':
    exam_1()
    exam_2()
    exam_3()
    exam_4()
    exam_5()
