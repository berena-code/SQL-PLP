CREATE DATABASE inventory;

USE inventory;

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) UNIQUE
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity_in_stock INT DEFAULT 0
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    order_date DATE,
    quantity_ordered INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE product_supplier (
    product_id INT,
    supplier_id INT,
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO suppliers (name, contact_email)
VALUES 
('Tech Supplies Ltd', 'info@techsupplies.com'),
('Office Essentials Co', 'contact@officeessentials.co.ke'),
('Smart Gadgets Hub', 'sales@smartgadgets.com'),
('Mega Electronics', 'support@megaelectronics.co.ke');

INSERT INTO products (name, price, quantity_in_stock)
VALUES 
('Laptop', 800.00, 10),
('Printer', 250.00, 5),
('Wireless Mouse', 20.00, 50),
('Office Chair', 100.00, 15),
('Monitor 24"', 150.00, 20);

INSERT INTO product_supplier (product_id, supplier_id)
VALUES 
(1, 1),  -- Laptop from Tech Supplies
(2, 2),  -- Printer from Office Essentials
(3, 3),  -- Mouse from Smart Gadgets
(4, 2),  -- Chair from Office Essentials
(5, 4),  -- Monitor from Mega Electronics
(3, 1),  -- Mouse also available from Tech Supplies
(5, 1);  -- Monitor also from Tech Supplies

INSERT INTO orders (product_id, order_date, quantity_ordered)
VALUES 
(1, '2025-04-20', 2),  -- 2 Laptops
(3, '2025-04-21', 5),  -- 5 Mice
(5, '2025-04-21', 3),  -- 3 Monitors
(2, '2025-04-22', 1),  -- 1 Printer
(4, '2025-04-22', 4);  -- 4 Chairs