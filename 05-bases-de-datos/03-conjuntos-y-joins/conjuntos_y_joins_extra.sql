-- 1. Explicación cruzada entre conjuntos y SQL

-- Analice la operación de conjuntos All - Odd.

-- R/ Significa obtener todos los numeros que esta en All pero no estan en Odd

-- Explique cómo una operación similar se puede representar en SQL con JOINs.

-- R/ En SQL esto se utiliza cuando queremos obtener registros de una tabla que no tienen
-- coincidencia en otra tabla.

-- ¿Qué tipo de JOIN usaría?

-- R/ Usaria LEFT JOIN porque necesito traer todos los registros de la tabla principal (All)
-- Ver cuáles no existen en la segunda tabla (Odd)


-- 2. Agrupamiento y conteo cruzado

-- Usando las tablas de Books, Customers y Rents:

-- Obtenga el número total de veces que cada cliente ha rentado un libro

-- Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
-- Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT

SELECT 
    c.ID,
    c.Name,
    COUNT(r.ID) AS TotalRents
FROM Customers c
INNER JOIN Rents r
ON c.ID = r.CustomerID
GROUP BY c.ID, c.Name
ORDER BY TotalRents DESC
LIMIT 3;


-- 3. Consulta con múltiples JOINS anidados
-- Genere un SELECT que devuelva lo siguiente:
-- Nombre del cliente
-- Nombre del libro
-- Nombre del autor
-- Estado del alquiler (Rents.State)
-- Debe manejar el caso en que un libro no tenga autor

SELECT 
    c.Name AS CustomerName,
    b.Name AS BookName,
    a.Name AS AuthorName,
    r.State AS RentState
FROM Rents r
INNER JOIN Customers c
    ON r.CustomerID = c.ID
INNER JOIN Books b
    ON r.BookID = b.ID
LEFT JOIN Authors a
    ON b.Author = a.ID;