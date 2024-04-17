#!/usr/bin/python3


def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0
