-- SQL script to insert sample data
-- inserting sample data into Customers table
INSERT INTO Customer (name, email, join_date)
VALUES (
        'Richard Edim',
        'richaardedim@gmail.com',
        '2024-02-10'
    ),
    (
        'Mary Johnson',
        'mary.johnson@gmail.com',
        '2024-03-05'
    ),
    (
        'David Emmanuel',
        'davidemmanuel@gmail.com',
        '2024-04-12'
    ),
    (
        'Esther Williams',
        'estherwilliams@gmail.com',
        '2024-05-18'
    ),
    (
        'Michael Bissong',
        'michaelbissong@gmail.com',
        '2024-06-21'
    );
-- inserting sample data into Products table
INSERT INTO Product (product_name, category, price)
VALUES ('Wireless Mouse', 'Electronics', 25.50),
    ('Bluetooth Headphones', 'Electronics', 89.99),
    ('Yoga Mat', 'Fitness', 30.00),
    ('Leather Wallet', 'Accessories', 45.25),
    (
        'Stainless Steel Water Bottle',
        'Home & Kitchen',
        22.75
    );
-- inserting sample data into Orders table
INSERT INTO Orders (customer_id, product_id, quantity, order_date)
VALUES (1, 2, 1, '2024-06-01'),
    (2, 1, 2, '2024-06-02'),
    (3, 3, 1, '2024-06-05'),
    (4, 5, 3, '2024-06-08'),
    (5, 4, 1, '2024-06-10');