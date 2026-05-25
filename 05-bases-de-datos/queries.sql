-- Replique las tablas creadas anteriormente en Ejercicio de Bases de Datos

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  registration_date TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE shopping_cart (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_user INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  brand TEXT NOT NULL,
  price REAL NOT NULL,
  stock_available INTEGER NOT NULL,
  entry_date TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  comment TEXT NOT NULL,
  rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  comment_date TEXT DEFAULT CURRENT_TIMESTAMP,
  product_code INTEGER NOT NULL REFERENCES products(id),
  id_user INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE payment_methods (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  method_type TEXT NOT NULL,
  bank_name TEXT NOT NULL,
  id_owner INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE invoices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  invoice_number TEXT NOT NULL,
  purchase_date TEXT DEFAULT CURRENT_TIMESTAMP,
  total_amount REAL NOT NULL,
  id_buyer INTEGER NOT NULL REFERENCES users(id),
  id_payment_method INTEGER NOT NULL REFERENCES payment_methods(id)
);

CREATE TABLE shopping_cart_products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_shopping_cart INTEGER NOT NULL REFERENCES shopping_cart(id),
  id_product INTEGER NOT NULL REFERENCES products(id)
);

CREATE TABLE invoice_products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_product INTEGER NOT NULL REFERENCES products(id),
  id_invoice INTEGER NOT NULL REFERENCES invoices(id),
  quantity INTEGER NOT NULL,
  subtotal REAL NOT NULL
);

-- Utilizando el comando ALTER, modifique la tabla de Facturas y agregue una columna para almacenar también
-- el número de teléfono del comprador, y otra para el código de empleado del cajero que realizó la venta.

ALTER TABLE invoices
ADD COLUMN buyer_phone TEXT;

ALTER TABLE invoices
ADD COLUMN cashier_code INTEGER;

-- Obtenga todos los productos almacenados
SELECT * FROM products;

-- Obtenga todos los productos que tengan un precio mayor a 50000
SELECT *
FROM products
WHERE price > 50000;

-- Obtenga todas las compras de un mismo producto por id.
SELECT *
FROM invoice_products
WHERE id_product = 1;

-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT
  id_product,
  SUM(quantity) AS total_comprado
FROM invoice_products
GROUP BY id_product;

-- Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM invoices
WHERE id_buyer = 1;

-- Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM invoices
ORDER BY total_amount DESC;

-- Obtenga una sola factura por número de factura.
SELECT *
FROM invoices
WHERE invoice_number = 'FAC-1001';