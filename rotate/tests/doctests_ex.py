"""Tests using doctest.

Report:
    python doctests_ex.py -v > doctests_report.txt


>>> reading.from_file(this_dir+r'\\ex1.txt', this_dir+r'\\save1.txt', ciphers.rot_13)
The file is saved

>>> reading.from_file(this_dir+r'\\ex2.txt', this_dir+r'\\save2.txt', ciphers.caesar_1)
The file is saved

>>> reading.from_file(this_dir+r'\\ex3.txt', this_dir+r'\\save3.txt')
The file is saved

>>> reading.from_string('reebe', alg=ciphers.rot_13)
'error'

>>> ciphers.rot_13('Q')
'D'

"""


import doctest
import os
import sys


up = os.path.dirname
sys.path.append(up(up(up(os.path.abspath(__file__)))))
this_dir = up(up(up(os.path.abspath(__file__)))) + r'\\Examples'

# Only in this order
from rotate import reading, ciphers

doctest.testmod(verbose=True)
