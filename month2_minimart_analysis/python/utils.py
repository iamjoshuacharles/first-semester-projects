
# utils.py

def calculate_total(price, quantity):
    """Calculate total order amount."""
    return round(price * quantity, 2)


def is_large_order(total):
    """Flag order as large if total > $100."""
    return total > 100


def convert_currency(price_usd, rate=1600):
    """Convert USD price to another currency (default: Naira)."""
    return round(price_usd * rate, 2)


def apply_discount(price, threshold=80, discount_rate=0.1):
    """Apply discount for products above price threshold."""
    if price > threshold:
        return round(price * (1 - discount_rate), 2)
    return price
