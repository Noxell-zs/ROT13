"""Tests using doctest.

Report:
    python doctests_ex.py -v > doctests_report.txt


>>> reading.from_file(this_dir+r'\\ex1.txt', this_dir+r'\\save1.txt', ciphers.rot13)
The file is saved

>>> reading.from_file(this_dir+r'\\ex2.txt', this_dir+r'\\save2.txt', ciphers.caesar1)
The file is saved

>>> reading.from_file(this_dir+r'\\ex3.txt', this_dir+r'\\save3.txt')
The file is saved

>>> reading.from_string('reebe', alg=ciphers.rot13)
'error'

>>> ciphers.rot13('Q')
'D'

"""


if __name__ == '__main__':
    import doctest
    import os
    from rotate import reading, ciphers

    up = os.path.dirname
    this_dir = up(up(up(os.path.abspath(__file__)))) + r'\\Examples'

    doctest.testmod(verbose=True)
