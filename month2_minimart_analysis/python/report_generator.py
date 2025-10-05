# report_generator.py

import json

def generate_report(orders, customers, products):
    """Generate summary report from order data."""

    # Total products sold
    total_products_sold = sum(order["quantity"] for order in orders)

    # Revenue per customer
    revenue_per_customer = {}
    for order in orders:
        customer_name = customers[order["customer_id"]]
        revenue_per_customer[customer_name] = revenue_per_customer.get(customer_name, 0) + order["total_price"]

    # Product sales count
    product_sales = {}
    for order in orders:
        pid = order["product_id"]
        product_sales[pid] = product_sales.get(pid, 0) + order["quantity"]

    # Most popular product
    most_popular_product_id = max(product_sales, key=product_sales.get)
    most_popular_product = products[most_popular_product_id]["product_name"]

    # Create final report
    report = {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular_product,
        "revenue_per_customer": revenue_per_customer,
    }

    return report


def save_report_to_json(report, filename="sales_report.json"):
    """Save report to a JSON file."""
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)


def print_report(report):
    """Nicely format and display the report."""
    print("....Sales Summary Report....")
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"Most Popular Product: {report['most_popular_product']}")
    print("\nRevenue per Customer:")
    for customer, revenue in report["revenue_per_customer"].items():
        print(f" - {customer}: ${revenue:.2f}")

    print("\n....End of Report....")
