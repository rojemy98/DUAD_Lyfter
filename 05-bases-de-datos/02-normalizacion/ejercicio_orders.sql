-- TABLA SIN NORMALIZAR

-- Problemas:
-- - Datos repetidos
-- - Difícil mantenimiento

CREATE TABLE order_data_unnormalized (
    order_id TEXT,
    customer_name TEXT,
    customer_phone TEXT,
    address TEXT,
    item_id INTEGER,
    item_name TEXT,
    price REAL,
    quantity INTEGER,
    special_request TEXT,
    delivery_time TEXT
);


INSERT INTO order_data_unnormalized VALUES
('001', 'Alice', '123-456-7890', '123 Main St', 101, 'Cheeseburger', 8.00, 2, 'No onions', '6:00 PM'),

('001', 'Alice', '123-456-7890', '123 Main St', 102, 'Fries', 3.00, 1, 'Extra ketchup', '6:00 PM'),

('002', 'Bob', '987-654-3210', '456 Elm St', 103, 'Pizza', 12.00, 1, 'Extra cheese', '7:30 PM'),

('002', 'Bob', '987-654-3210', '4th Avenue', 102, 'Fries', 3.00, 2, 'None', '7:30 PM'),

('003', 'Claire', '555-123-4567', '789 Oak St', 105, 'Salad', 6.00, 1, 'No croutons', '12:00 PM'),

('004', 'Claire', '555-123-4567', '464 Georgia St', 106, 'Water', 1.00, 1, 'None', '5:00 PM');



-- PRIMERA FORMA NORMAL (1NF)

-- Reglas:
-- - Valores atómicos
-- - Sin grupos repetidos

-- PK:
-- (order_id, item_id)

CREATE TABLE order_data_1nf (
    order_id TEXT,
    item_id INTEGER,

    customer_name TEXT,
    customer_phone TEXT,
    address TEXT,
    delivery_time TEXT,

    item_name TEXT,
    price REAL,

    quantity INTEGER,
    special_request TEXT,

    PRIMARY KEY (order_id, item_id)
);


INSERT INTO order_data_1nf (
    order_id,
    item_id,
    customer_name,
    customer_phone,
    address,
    delivery_time,
    item_name,
    price,
    quantity,
    special_request
)
SELECT
    order_id,
    item_id,
    customer_name,
    customer_phone,
    address,
    delivery_time,
    item_name,
    price,
    quantity,
    special_request
FROM order_data_unnormalized;



-- Problema:
-- Dependencias parciales
--
-- order_id --> pedido
-- item_id --> producto



-- SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- - Productos
-- - Pedidos
-- - Detalles



-- PRODUCTS_2NF

CREATE TABLE products_2nf (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT,
    price REAL
);


INSERT INTO products_2nf (
    item_id,
    item_name,
    price
)
SELECT DISTINCT
    item_id,
    item_name,
    price
FROM order_data_1nf;



-- ORDERS_2NF

CREATE TABLE orders_2nf (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    customer_phone TEXT,
    address TEXT,
    delivery_time TEXT
);


INSERT INTO orders_2nf (
    order_id,
    customer_name,
    customer_phone,
    address,
    delivery_time
)
SELECT DISTINCT
    order_id,
    customer_name,
    customer_phone,
    address,
    delivery_time
FROM order_data_1nf;



-- ORDER_DETAILS_2NF

CREATE TABLE order_details_2nf (
    order_id TEXT,
    item_id INTEGER,

    quantity INTEGER,
    special_request TEXT,

    PRIMARY KEY (order_id, item_id),

    FOREIGN KEY (order_id)
        REFERENCES orders_2nf(order_id),

    FOREIGN KEY (item_id)
        REFERENCES products_2nf(item_id)
);


INSERT INTO order_details_2nf (
    order_id,
    item_id,
    quantity,
    special_request
)
SELECT
    order_id,
    item_id,
    quantity,
    special_request
FROM order_data_1nf;



-- Problema:
-- Clientes repetidos
-- Dependencia transitiva



-- TERCERA FORMA NORMAL (3NF)

-- Crear customers



-- CUSTOMERS

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    customer_phone TEXT
);


INSERT INTO customers (
    customer_name,
    customer_phone
)
SELECT DISTINCT
    customer_name,
    customer_phone
FROM orders_2nf;



-- ORDERS FINAL

CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,

    customer_id INTEGER,

    address TEXT,
    delivery_time TEXT,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


INSERT INTO orders (
    order_id,
    customer_id,
    address,
    delivery_time
)
SELECT
    o.order_id,
    c.customer_id,
    o.address,
    o.delivery_time
FROM orders_2nf o
JOIN customers c
    ON o.customer_phone = c.customer_phone;



-- PRODUCTS FINAL

CREATE TABLE products (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT,
    price REAL
);


INSERT INTO products (
    item_id,
    item_name,
    price
)
SELECT
    item_id,
    item_name,
    price
FROM products_2nf;



-- ORDER_DETAILS FINAL

CREATE TABLE order_details (
    order_id TEXT,
    item_id INTEGER,

    quantity INTEGER,
    special_request TEXT,

    PRIMARY KEY (order_id, item_id),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (item_id)
        REFERENCES products(item_id)
);


INSERT INTO order_details (
    order_id,
    item_id,
    quantity,
    special_request
)
SELECT
    order_id,
    item_id,
    quantity,
    special_request
FROM order_details_2nf;



-- RESULTADO FINAL

-- customers
-- orders
-- products
-- order_details