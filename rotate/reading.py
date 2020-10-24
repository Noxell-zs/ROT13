"""Realization of ways to read and write text.

Functions:
    from_file(functions)
        Reading text from a file.
    from_string(functions)
        Reading text from a argument.

"""


import os.path


def from_file(
        read_path,
        write_path,
        alg=lambda x: x,
):
    """Reading text from a file.

    The user enters the name of the file to open.  If a file with this
    name does not exist: message output, the function returns None.
    Otherwise, the text from the file is saved to a variable.  Enter
    the name of the file to save.  The encryption result is written to
    it character by character.

    Parameters:
        read_path : str
            Full path of the file to open.
        write_path : str
            Full path of the file to save.
        alg : function
            Algorithm that processes text characters.  Returns the
            original character by default.
    
    Returns:
        None

    """
    if not os.path.isfile(read_path):
        print(f'{read_path} file was not found')
        return None

    with open(read_path, 'r') as r:
        text = r.read()

    with open(write_path, 'w') as w:
        for ch in text:
            w.write(alg(ch))

    print(f'The file is saved')


def from_string(str_in, alg=lambda x: x):
    """Reading text passed as an argument.

    Parameters:
        str_in : str
            Any sequence of characters.
        alg : function
            Algorithm that processes text characters.  Returns the
            original character by default.

    Returns:
        str_out : str
            The encrypted sequence of characters.

    """
    str_out = ''
    for ch in str_in:
        str_out += alg(ch)

    return str_out
