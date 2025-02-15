def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit or vice versa.

    Parameters:
    value (float): The temperature value to convert.
    from_unit (str): The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit).
    to_unit (str): The unit to convert to ('C' for Celsius, 'F' for Fahrenheit).

    Returns:
    float: The converted temperature value.

    Raises:
    ValueError: If an invalid unit is provided.

    Example Usage:
    >>> convert_temperature(100, 'C', 'F')
    212.0
    >>> convert_temperature(32, 'F', 'C')
    0.0
    """
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

# Example 
temperature = float(input("Enter the temperature value: "))
origin_unit = input("Enter the current unit (C/F): ").upper()
target_unit = input("Enter the target unit (C/F): ").upper()

try:
    converted_temp = convert_temperature(temperature, origin_unit, target_unit)
    print(f"The converted temperature is: {converted_temp:.2f}°{target_unit}")
except ValueError as e:
    print(f"Error: {e}")
