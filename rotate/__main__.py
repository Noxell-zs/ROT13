"""Cipher ROT13

Reading text from a file.
The file is encrypted using the ROT13 algorithm.
Saving text to a file.

Algorithm description:
https://ru.wikipedia.org/wiki/ROT13

-------

    python -m rotate
    pip install -i https://test.pypi.org/simple/ rotate

:Authors:
    Замолоцкий Семен Андреевич, КИ20-17/1б

"""


from rotate import reading, ciphers


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
                              alg=ciphers.rot13)

        elif enter in ('c', 'console'):
            print(reading.from_string(input('Enter the text: '),
                                      alg=ciphers.rot13))

        else:
            print(f'A nonexistent command {enter} was entered')
        print()


if __name__ == '__main__':
    main()
