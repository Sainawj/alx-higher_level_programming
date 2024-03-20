#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_values[char]
        result += value if value >= prev_value else -value
        prev_value = value

    return result

