# Entry point for the MiniMart data reporting system

# main.py

from utils import calculate_total, is_large_order, convert_currency, apply_discount
from report_generator import generate_report, save_report_to_json, print_report

# Sample product data
products = {
    1: {"product_name": "Wireless Mouse", "category": "Electronics", "price": 25.50},
    2: {"product_name": "Bluetooth Headphones", "category": "Electronics", "price": 89.99},
    3: {"product_name": "Yoga Mat", "category": "Fitness", "price": 30.00},
    4: {"product_name": "Leather Wallet", "category": "Accessories", "price": 45.25},
    5: {"product_name": "Steel Water Bottle", "category": "Home & Kitchen", "price": 22.75}
}

# Sample customer data
customers = {
    1: "Richard Edim",
    2: "Mary Johnson",
    3: "David Emmanuel",
    4: "Esther Williams",
    5: "Michael Bissong"
}

# Simulated orders
orders = [
    {"customer_id": 1, "product_id": 2, "quantity": 1},
    {"customer_id": 2, "product_id": 1, "quantity": 3},
    {"customer_id": 3, "product_id": 4, "quantity": 2},
    {"customer_id": 4, "product_id": 3, "quantity": 1},
    {"customer_id": 5, "product_id": 5, "quantity": 5}
]

# Step 1: Process orders
for order in orders:
    product = products[order["product_id"]]
    total = calculate_total(product["price"], order["quantity"])
    order["total_price"] = total
    order["large_order"] = is_large_order(total)

# Step 2: Convert prices to Naira and apply discounts
for product in products.values():
    product["price_naira"] = convert_currency(product["price"])
    product["discounted_price"] = apply_discount(product["price"])

# Step 3: Generate and display report
report = generate_report(orders, customers, products)

# Step 4: Save to JSON and print summary
save_report_to_json(report)
print_report(report)
