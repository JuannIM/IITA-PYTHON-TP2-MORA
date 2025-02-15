def convert_to_character_lists(words: list[str]) -> list[list[str]]:
    """
    Converts a list of strings into a list of character lists.

    Parameters:
    words (list[str]): A list of words to be converted.

    Returns:
    list[list[str]]: A list where each word is transformed into a list of its characters.

    Example:
    >>> convert_to_character_lists(["hola", "adios"])
    [['h', 'o', 'l', 'a'], ['a', 'd', 'i', 'o', 's']]
    """
    return list(map(list, words))

def get_user_words() -> list[str]:
    """
    Prompts the user to enter words and returns them as a list.

    Returns:
    list[str]: A list of words entered by the user.
    """
    words = input("Enter words separated by spaces: ").split()
    return words

# Example 
words_list = ["hola", "adios"]
print(convert_to_character_lists(words_list))

# Main program execution
user_words = get_user_words()
converted_list = convert_to_character_lists(user_words)

print("\nConverted List:", converted_list)
