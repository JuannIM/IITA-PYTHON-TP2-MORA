def update_inventory(inventory: dict[str, int], sold_items: list[str]) -> dict[str, int]:
    """
    Updates the inventory of a store by reducing the stock of sold products.

    Parameters:
    inventory (dict[str, int]): A dictionary where keys are product names and values are their stock quantities.
    sold_items (list[str]): A list of product names representing the items sold.

    Returns:
    dict[str, int]: The updated inventory after deducting the sold items.

    Example Usage:
    >>> inventory = {"apple": 10, "banana": 5, "orange": 8}
    >>> sold_items = ["apple", "banana", "banana", "orange", "orange", "orange"]
    >>> update_inventory(inventory, sold_items)
    {'apple': 9, 'banana': 3, 'orange': 5}
    """
    for item in sold_items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1  # Reduce stock by 1 for each sold item
        elif item in inventory and inventory[item] == 0:
            print(f"Warning: {item} is out of stock.")
        else:
            print(f"Warning: {item} is not in the inventory.")

    return inventory

def get_inventory() -> dict[str, int]:
    """
    Prompts the user to enter store inventory.

    Returns:
    dict[str, int]: A dictionary containing product names and their stock quantities.
    """
    inventory = {}
    print("\nEnter store inventory (Enter 'done' to finish):")
    while True:
        product = input("Product name: ").strip()
        if product.lower() == "done":
            break
        try:
            quantity = int(input(f"Enter stock for {product}: "))
            if quantity < 0:
                print("Quantity must be a positive number.")
                continue
            inventory[product] = quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return inventory

def get_sold_items() -> list[str]:
    """
    Prompts the user to enter sold items.

    Returns:
    list[str]: A list containing the names of sold products.
    """
    sold_items = []
    print("\nEnter sold products (Enter 'done' to finish):")
    while True:
        product = input("Sold product name: ").strip()
        if product.lower() == "done":
            break
        sold_items.append(product)
    
    return sold_items

# Main program execution
store_inventory = get_inventory()
products_sold = get_sold_items()

updated_inventory = update_inventory(store_inventory, products_sold)

print("\nUpdated Inventory:", updated_inventory)
