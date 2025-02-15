def is_palindrome(text: str) -> bool:
    """
    Checks if a given word or phrase is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward,
    ignoring spaces, punctuation, and capitalization.

    Parameters:
    text (str): The input string to check.

    Returns:
    bool: True if the input is a palindrome, False otherwise.

    Example Usage:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("A man a plan a canal Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    # Normalize the text: remove spaces and convert to lowercase
    normalized_text = "".join(text.lower().split())

    # Compare the string with its reverse
    return normalized_text == normalized_text[::-1]

# Example 
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
