"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    """Add an item to the basket and return the updated basket."""
    for existing_item in basket:
        if existing_item["name"] == item["name"] and \
                existing_item["price"] == item["price"]:
            existing_item["count"] += 1
            return basket

    basket.append({"name": item["name"], "price": item["price"], "count": 1})
    return basket


def generate_receipt(item_basket: list) -> str:
    """Generate a formatted receipt string from a list of basket items."""
    if not item_basket:
        return "Basket is empty"

    lines = []
    total_cost = 0

    for item in item_basket:
        item_name = item["name"]
        item_price = item["price"]
        item_count = item["count"]

        multiple_items_cost = item_price * item_count
        total_cost += multiple_items_cost

        item_price_str = "Free" if item_price == 0 else f"£{multiple_items_cost:.2f}"
        lines.append(f"{item_name} x {item_count} - {item_price_str}")

    lines.append(f"Total: £{total_cost:.2f}")
    return "\n".join(lines)

# cle
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
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
