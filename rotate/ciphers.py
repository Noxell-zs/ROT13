"""Realization of algorithms for char-by-char text encryption.

Functions:
    rot_13(str) -> str
        Character offset by 13 positions.
    caesar_1(str) -> str
        Character offset by 1 position.

"""


def rot_13(char_in: str) -> str:
    """Character offset by 13 positions.

    Parameters:
        char_in : function
            Character of the source text.

    Returns:
        char_out : str
            Character of the encrypted text.

    """
    num = ord(char_in[0])

    if (97 <= num <= 109) or (65 <= num <= 77):
        char_out = chr(num + 13)
    elif (110 <= num <= 122) or (78 <= num <= 90):
        char_out = chr(num - 13)
    else:
        char_out = char_in

    return char_out


def caesar_1(char_in: str) -> str:
    """Character offset by 1 position.

    Parameters:
        char_in : function
            Character of the source text.

    Returns:
        char_out : str
            Character of the encrypted text.

    """
    num = ord(char_in[0])

    if (97 <= num <= 121) or (65 <= num <= 89):
        char_out = chr(num + 1)
    elif num == 122 or num == 90:
        char_out = chr(num - 25)
    else:
        char_out = char_in

    return char_out
