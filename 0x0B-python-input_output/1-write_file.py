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
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0

# Example usage:
if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
