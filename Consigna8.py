from statistics import mean, median, mode

def calculate_statistics(numbers: list[float]) -> dict[str, float]:
    """
    Calculates the mean, median, and mode of a given list of numbers.

    Parameters:
    numbers (list[float]): A list of numerical values.

    Returns:
    dict[str, float]: A dictionary containing:
        - 'mean': The average value (sum of numbers divided by the count).
        - 'median': The middle value when numbers are sorted.
        - 'mode': The most frequently occurring number.

    Example:
    >>> calculate_statistics([1, 2, 2, 3, 4])
    {'mean': 2.4, 'median': 2, 'mode': 2}
    """
    return {
        "mean": mean(numbers),
        "median": median(numbers),
        "mode": mode(numbers)
    }

# Example 
numbers_list = [1, 2, 2, 3, 4]
print(calculate_statistics(numbers_list))

def get_user_numbers() -> list[float]:
    """
    Prompts the user to enter a list of numbers separated by spaces.

    Returns:
    list[float]: A list of numerical values entered by the user.
    """
    while True:
        try:
            numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
            if not numbers:
                raise ValueError("You must enter at least one number.")
            return numbers
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")

# Main program execution
user_numbers = get_user_numbers()
stats = calculate_statistics(user_numbers)

print("\nStatistics:")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")
