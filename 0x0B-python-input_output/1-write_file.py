def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Default is an empty string.
        text (str): The text to write into the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    '''
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
            return num_chars_written
    except Exception as e:
        print(f"Error occurred: {e}")
        return (0)
