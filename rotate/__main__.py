"""Cipher ROT13

Reading text from a file.
The file is encrypted using the ROT13 algorithm.
Saving text to a file.

Algorithm description:
https://ru.wikipedia.org/wiki/ROT13


For doctest:

>>> reading.from_string('Original text')
'Original text'

>>> reading.from_string('AbcdE', alg=ciphers.caesar_1)
'BcdeF'

>>> reading.from_string('reebe', alg=ciphers.rot_13)
'error'

>>> ciphers.rot_13('Q')
'D'

>>> ciphers.caesar_1('z')
'a'


Install the package:
    pip install -i https://test.pypi.org/simple/ rotate
Run the main program:
    python -m rotate
Run tests using doctest:
    python -m rotate --doctest [> rotate\\tests\\doctests_report.txt]
Run tests using pytest:
    python -m rotate --pytest [> rotate\\tests\\pytests_report.txt]


:Authors:
    Замолоцкий Семен Андреевич, КИ20-17/1б

"""


import argparse
import os.path
from rotate import reading, ciphers


parser = argparse.ArgumentParser(description='Enter pytest or doctest mode')
parser.add_argument('-p', '--pytest', required=False, action='store_const',
                    const=True, help='Run tests using pytest')
parser.add_argument('-d', '--doctest', required=False, action='store_const',
                    const=True, help='Run tests using doctest')
args = parser.parse_args()


def cli():
    """Realization of Command Line Interface."""
    if args.doctest:
        import doctest
        doctest.testmod(verbose=True)

    if args.pytest:
        import pytest
        this_dir = os.path.dirname(os.path.abspath(__file__))
        pytest.main(args=['-v', this_dir])


def info():
    """Output information about available commands."""
    print()
    print('EXIT for end the program')
    print('FILE for reading text from a file')
    print('CONSOLE for reading text from the console')


def main():
    msg_info = 'Enter the command (INFO for information): '
    msg_open = 'Enter the FULL path of the text file '

    while (enter := input(msg_info).lower()) not in ('exit', 'e'):

        if enter in ('i', 'info'):
            info()

        elif enter in ('f', 'file'):
            reading.from_file(input(msg_open + 'for reading: '),
                              input(msg_open + 'for saving: '),
                              alg=ciphers.rot_13)

        elif enter in ('c', 'console'):
            print(reading.from_string(input('Enter the text: '),
                                      alg=ciphers.rot_13))

        else:
            print(f'A nonexistent command {enter} was entered')
        print()


if __name__ == '__main__':
    if args.doctest or args.pytest:
        cli()
    else:
        main()
