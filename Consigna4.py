def analyze_text(text: str) -> dict[str, int]:
    """
    Analyzes a given text and returns the number of words and characters.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    dict[str, int]: A dictionary containing:
        - "word_count" (int): The number of words in the text.
        - "char_count" (int): The number of characters (excluding spaces) in the text.

    Example Usage:
    >>> analyze_text("Hello world!")
    {'word_count': 2, 'char_count': 10}
    
    >>> analyze_text("Python is awesome.")
    {'word_count': 3, 'char_count': 16}
    """
    words = text.split()  # Split the text into words based on spaces
    char_count = len(text.replace(" ", ""))  # Count characters excluding spaces

    return {
        "word_count": len(words),
        "char_count": char_count
    }

# Example 
user_text = input("Enter a text: ")
result = analyze_text(user_text)

print(f"Word count: {result['word_count']}")
print(f"Character count (excluding spaces): {result['char_count']}")
