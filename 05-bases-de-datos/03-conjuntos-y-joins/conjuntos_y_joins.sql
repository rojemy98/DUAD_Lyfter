-- Habilitar llaves foráneas en SQLite
PRAGMA foreign_keys = ON;

-- Crear tabla Authors
CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

-- Crear tabla Books
CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Author INTEGER,
    FOREIGN KEY (Author) REFERENCES Authors(ID)
);

-- Crear tabla Customers
CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);

-- Crear tabla Rents
CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER NOT NULL,
    CustomerID INTEGER NOT NULL,
    State TEXT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);

-- Insertar datos en Authors
INSERT INTO Authors (ID, Name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

-- Insertar datos en Books
INSERT INTO Books (ID, Name, Author) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

-- Insertar datos en Customers
INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

-- Insertar datos en Rents
INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


-- Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT b.Name, a.Name
FROM Books b
INNER JOIN Authors a
ON a.ID = b.ID

-- Obtenga todos los libros que no tienen autor
SELECT b.ID, b.Name, a.Name
FROM Books b
LEFT JOIN Authors a
ON b.Author = a.ID
WHERE b.Author IS NULL;

-- Obtenga todos los autores que no tienen libros
SELECT a.ID, a.Name, b.Name
FROM Books b
RIGHT JOIN Authors a
ON b.Author = a.ID
WHERE B.Author IS NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT b.ID, b.Name, r.State
FROM Books b 
INNER JOIN Rents r 
ON b.ID = r.BookID

-- Obtenga todos los libros que nunca han sido rentados
SELECT b.ID, b.Name, r.State
FROM Books b 
LEFT JOIN Rents r 
ON b.ID = r.BookID
WHERE r.State is NULL

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT c.ID, c.Name
FROM Customers c 
LEFT JOIN Rents r 
ON c.ID = r.CustomerID 
WHERE r.CustomerID is NULL

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT b.ID, b.Name, r.State
FROM Books b 
LEFT JOIN Rents r 
on b.ID = r.BookID 
WHERE r.State = 'Overdue';