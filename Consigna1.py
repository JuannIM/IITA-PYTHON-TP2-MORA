def calculate_discount(price: float, discount: float) -> float:
    """
    Calculates the final price of a product after applying a discount.

    Parameters:
    price (float): The original price of the product.
    discount (float): The discount percentage to apply (0-100).

    Returns:
    float: The final price after applying the discount.
    """
    final_price = price - (price * (discount / 100))
    return final_price

# Example
original_price = float(input("Enter the product price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after discount is: {final_price:.2f}")
