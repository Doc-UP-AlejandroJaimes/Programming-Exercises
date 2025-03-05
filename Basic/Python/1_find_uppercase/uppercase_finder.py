def find_uppercase(string: str) -> str:
    """
    Extracts and returns all uppercase letters from a given string.

    Parameters:
    string (str): The input string to process.

    Returns:
    str: A string containing only the uppercase letters from the input string.
    
    Example:
    >>> find_uppercase("Hello World!")
    'HW'
    """
    uppercase_letters = ""
    for char in string:
        if char.isupper():
            uppercase_letters = uppercase_letters + char
    return uppercase_letters
