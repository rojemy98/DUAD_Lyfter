-- Tarea 2: Pruebas básicas de la DB


-- Con la DB creada, cree los siguientes scripts:

-- Un script que agregue un usuario nuevo

INSERT INTO lyfter_car_rental.users
(
    name,
    last_name,
    username,
    email,
    password,
    birthdate
)
VALUES
(
    'Rojemy',
    'Emanuel',
    'rojemy',
    'rojemy@email.com',
    'SecurePass123!',
    '1998-06-11'
);

-- Un script que agregue un automovil nuevo

INSERT INTO lyfter_car_rental.cars
(
    brand,
    model,
    manufacturing_year
)
VALUES
(
    'Toyota',
    'Corolla',
    2024
);

-- Un script que cambie el estado de un usuario

UPDATE lyfter_car_rental.users
SET status = 'Inactive'
WHERE id = 5;

-- Un script que cambie el estado de un automovil

UPDATE lyfter_car_rental.cars
SET status = 'Maintenance'
WHERE id = 3;

-- Un script que genere un alquiler nuevo con los datos de un usuario y un automovil

BEGIN;

INSERT INTO lyfter_car_rental.rentals
(user_id, car_id)
VALUES
(1, 2);

UPDATE lyfter_car_rental.cars
SET status = 'Rented'
WHERE id = 2;

COMMIT;


-- Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler

BEGIN;

UPDATE lyfter_car_rental.cars
SET status = 'Available'
WHERE id =
(
    SELECT car_id
    FROM lyfter_car_rental.rentals
    WHERE id = 10
);

UPDATE lyfter_car_rental.rentals
SET rental_status = 'Completed'
WHERE id = 10;

COMMIT;

-- Un script que deshabilite un automovil del alquiler

UPDATE lyfter_car_rental.cars
SET status = 'Maintenance'
WHERE id = 7;

-- Un script que obtenga todos los automoviles alquilados

SELECT
    id,
    brand,
    model,
    manufacturing_year,
    status
FROM lyfter_car_rental.cars
WHERE status = 'Rented'
ORDER BY brand, model;

-- y otro que obtenga todos los disponibles.

SELECT
    id,
    brand,
    model,
    manufacturing_year,
    status
FROM lyfter_car_rental.cars
WHERE status = 'Available'
ORDER BY brand, model;