#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    Example:
        >>> write_file("my_first_file.txt", "This School is so cool!\n")
        29
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters


# Test case
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
