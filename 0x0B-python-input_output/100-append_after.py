#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each found line.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
