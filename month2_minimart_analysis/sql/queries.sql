-- SQL queries for retrieving insights
-- Use SELECT to retrieve all customers or all products.
SELECT *
FROM Customer;
SELECT *
FROM Product -- listing all product in the product table
SELECT *
FROM Product
WHERE category = 'Electronics';
-- listing recent orders by date
SELECT *
FROM Orders ODER BY order_date DESC;
-- AGGREGATE QUERIES
-- using count to Find total number of orders
SELECT COUNT(*) AS total_orders
FROM Orders;
-- using sum to calculate revenue per product(price x quality)
SELECT p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM Orders o
    JOIN Product p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
-- finding the verage product price
SELECT AVG(price) AS average_product_price
FROM Product;
SELECT o.order_id,
    c.name AS customer_name,
    p.product_name,
    o.quality,
    p.price,
    (o.quality * p.price) AS total_amount,
    o.order_date
FROM Orders o
    INNER JOIN Customer c ON o.customer_id = c.customer_id
    INNER JOIN Product p ON o.product_id = p.product_id
    INNER JOIN Product p ON o.product_id = p.product_id
ORDER BY o.order_date;
-- left Join by listing all customers and their orders
SELECT c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date
FROM Customer c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;
-- left join by showing all products, including those not yet ordered
SELECT p.product_id,
    p.product_name,
    p.category,
    p.price,
    o.order_id
FROM Product p
    LEFT JOIN Orders o ON p.product_id = o.product_id
ORDER BY p.product_id;
-- the total revenue and order count
SELECT c.name AS customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.quantity * p.price) AS total_spent
FROM Customer c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id
    LEFT JOIN Product p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;