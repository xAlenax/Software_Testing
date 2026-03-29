# keep this OUTSIDE any class

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise ValueError("Quantity must be an integer")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    return True