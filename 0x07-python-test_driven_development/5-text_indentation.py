#!/usr/bin/python3
"""

This module defines a function that prints a text with 2 new lines after each of these characters: ., ? and :

"""
def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be printed

    Raises:
        TypeError: text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.strip()
   result = []
    skip_space = False

    for char in text:
        if char in ['.', '?', ':']:
            result.append(char)
            result.append('\n\n')
            skip_space = True
        elif char == ' ' and skip_space:
            continue
        else:
            result.append(char)
            skip_space = False

    print(''.join(result))
