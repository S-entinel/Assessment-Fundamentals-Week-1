
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    """Add an item to the basket and return the updated basket."""
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    """Generate a formatted receipt string from a list of basket items."""
    if not basket:
        return "Basket is empty"

    lines = []
    total_cost = 0

    for item in basket:
        item_name = item["name"]
        item_price = item["price"]
        total_cost += item_price

        item_price_str = "Free" if item_price == 0 else f"£{item_price:.2f}"
        lines.append(f"{item_name} - {item_price_str}")

    lines.append(f"Total: £{total_cost:.2f}")
    return "\n".join(lines)


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
