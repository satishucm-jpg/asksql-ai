CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_name, city, signup_date) VALUES
('John Smith', 'New York', '2024-01-10'),
('Priya Patel', 'Chicago', '2024-02-15'),
('David Lee', 'Dallas', '2024-03-20'),
('Maria Garcia', 'Austin', '2024-04-05');

INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 1200.00),
('Phone', 'Electronics', 800.00),
('Desk Chair', 'Furniture', 250.00),
('Monitor', 'Electronics', 350.00);

INSERT INTO orders (customer_id, product_id, order_date, quantity, total_amount) VALUES
(1, 1, '2024-04-01', 1, 1200.00),
(2, 2, '2024-04-05', 2, 1600.00),
(3, 3, '2024-04-10', 1, 250.00),
(4, 4, '2024-04-15', 3, 1050.00),
(1, 2, '2024-05-01', 1, 800.00),
(2, 4, '2024-05-08', 2, 700.00);