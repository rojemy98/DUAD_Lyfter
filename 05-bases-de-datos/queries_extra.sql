-- Crear categorías y ajustar productos

-- Cree la tabla categories con:
-- id (PK autoincrement)
-- name (UNIQUE, NOT NULL)
-- description

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  description TEXT
);

-- Agregue a products la columna category_id (INTEGER, puede permitir NULL)

ALTER TABLE products
ADD COLUMN category_id INTEGER REFERENCES categories(id);

--Inserte al menos 3 filas en categories

INSERT INTO categories (name, description) VALUES
('Electronics', 'Electronic devices and gadgets'),
('Clothing', 'Apparel and fashion'),
('Home', 'Home and kitchen products');

-- Actualice algunos products asignándoles un category_id

UPDATE products
SET category_id = 1
WHERE id IN (1,2,3,4,7,8,9);

UPDATE products
SET category_id = 2
WHERE id IN (5,6);

UPDATE products
SET category_id = 3
WHERE id IN (10);

-- Verifique con SELECT * FROM products (muestre id, product_name, price, category_id, stock_available)

SELECT id, name, price, category_id, stock_available
FROM products;

-- Carga de productos y filtros 

-- Inserte al menos 10 filas en products con product_name, price, stock_available

INSERT INTO products (name, brand, price, stock_available) VALUES
('Apple iPhone 14', 'Apple', 90000, 15),
('Samsung Galaxy S23', 'Samsung', 85000, 8),
('Apple MacBook Air', 'Apple', 120000, 5),
('Dell Laptop', 'Dell', 70000, 20),
('Nike Shoes', 'Nike', 60000, 12),
('Adidas T-Shirt', 'Adidas', 30000, 50),
('Apple Watch', 'Apple', 50000, 7),
('Headphones Sony', 'Sony', 45000, 30),
('Tablet Samsung', 'Samsung', 65000, 9),
('Gaming Chair', 'Generic', 55000, 4);

-- Seleccione todos los productos

SELECT * FROM products;

-- Seleccione productos con price > 50000

SELECT *
FROM products
WHERE price > 50000;

-- Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE

SELECT *
FROM products
WHERE name LIKE '%Apple%';

-- Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5

SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;

-- Correcciones de datos en productos

-- Establezca stock_available = 0 donde price <= 0

UPDATE products
SET stock_available = 0
WHERE price <= 0;

-- Aumente el price en 100 unidades para todos los productos cuando stock_available sea menor a 10

UPDATE products
SET price = price + 100
WHERE stock_available < 10;

-- Disminuya stock_available en 1 para un product_id específico

UPDATE products
SET stock_available = stock_available - 1
WHERE id = 1;

-- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10

SELECT *
FROM products
ORDER BY id ASC
LIMIT 10;