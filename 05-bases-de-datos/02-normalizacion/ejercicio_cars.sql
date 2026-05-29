-- TABLA SIN NORMALIZAR

-- Problemas:
-- - Datos repetidos
-- - Dificil mantenimiento

CREATE TABLE vehicle_data_unnormalized (
    vin TEXT,
    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT,

    owner_id INTEGER,
    owner_name TEXT,
    owner_phone TEXT,

    insurance_company TEXT,
    insurance_policy TEXT
);


INSERT INTO vehicle_data_unnormalized VALUES
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 101, 'Alice', '123-456-7890', 'ABC Insurance', 'Fire & Theft'),

('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 102, 'Bob', '987-654-3210', 'XYZ Insurance', 'Full Cover'),

('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue', 103, 'Claire', '555-123-4567', 'DEF Insurance', 'Collision'),

('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red', 104, 'Dave', '111-222-3333', 'GHI Insurance', 'Basic Legal');



-- PRIMERA FORMA NORMAL (1NF)

-- PK:
-- (vin, owner_id)

CREATE TABLE vehicle_data_1nf (
    vin TEXT,
    owner_id INTEGER,

    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT,

    owner_name TEXT,
    owner_phone TEXT,

    insurance_company TEXT,
    insurance_policy TEXT,

    PRIMARY KEY (vin, owner_id)
);


INSERT INTO vehicle_data_1nf (
    vin,
    owner_id,
    make,
    model,
    year,
    color,
    owner_name,
    owner_phone,
    insurance_company,
    insurance_policy
)
SELECT
    vin,
    owner_id,
    make,
    model,
    year,
    color,
    owner_name,
    owner_phone,
    insurance_company,
    insurance_policy
FROM vehicle_data_unnormalized;



-- Problema:
-- vin --> vehículo
-- owner_id --> dueño



-- SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- - Vehicles
-- - Owners
-- - Ownership



-- VEHICLES_2NF

CREATE TABLE vehicles_2nf (
    vin TEXT PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT
);


INSERT INTO vehicles_2nf (
    vin,
    make,
    model,
    year,
    color
)
SELECT DISTINCT
    vin,
    make,
    model,
    year,
    color
FROM vehicle_data_1nf;



-- OWNERS_2NF

CREATE TABLE owners_2nf (
    owner_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    owner_phone TEXT
);


INSERT INTO owners_2nf (
    owner_id,
    owner_name,
    owner_phone
)
SELECT DISTINCT
    owner_id,
    owner_name,
    owner_phone
FROM vehicle_data_1nf;



-- OWNERSHIP_2NF

CREATE TABLE ownership_2nf (
    vin TEXT,
    owner_id INTEGER,

    insurance_company TEXT,
    insurance_policy TEXT,

    PRIMARY KEY (vin, owner_id),

    FOREIGN KEY (vin)
        REFERENCES vehicles_2nf(vin),

    FOREIGN KEY (owner_id)
        REFERENCES owners_2nf(owner_id)
);


INSERT INTO ownership_2nf (
    vin,
    owner_id,
    insurance_company,
    insurance_policy
)
SELECT
    vin,
    owner_id,
    insurance_company,
    insurance_policy
FROM vehicle_data_1nf;



-- Problema:
-- Pólizas repetidas



-- TERCERA FORMA NORMAL (3NF)

-- Separar pólizas



-- INSURANCE_POLICIES

CREATE TABLE insurance_policies (
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,

    insurance_company TEXT,
    insurance_policy TEXT
);


INSERT INTO insurance_policies (
    insurance_company,
    insurance_policy
)
SELECT DISTINCT
    insurance_company,
    insurance_policy
FROM ownership_2nf;



-- VEHICLES FINAL

CREATE TABLE vehicles (
    vin TEXT PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT
);


INSERT INTO vehicles (
    vin,
    make,
    model,
    year,
    color
)
SELECT
    vin,
    make,
    model,
    year,
    color
FROM vehicles_2nf;



-- OWNERS FINAL

CREATE TABLE owners (
    owner_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    owner_phone TEXT
);


INSERT INTO owners (
    owner_id,
    owner_name,
    owner_phone
)
SELECT
    owner_id,
    owner_name,
    owner_phone
FROM owners_2nf;



-- OWNERSHIP FINAL

CREATE TABLE ownership (
    vin TEXT,
    owner_id INTEGER,
    policy_id INTEGER,

    PRIMARY KEY (vin, owner_id),

    FOREIGN KEY (vin)
        REFERENCES vehicles(vin),

    FOREIGN KEY (owner_id)
        REFERENCES owners(owner_id),

    FOREIGN KEY (policy_id)
        REFERENCES insurance_policies(policy_id)
);


INSERT INTO ownership (
    vin,
    owner_id,
    policy_id
)
SELECT
    o.vin,
    o.owner_id,
    p.policy_id
FROM ownership_2nf o
JOIN insurance_policies p
    ON o.insurance_company = p.insurance_company
   AND o.insurance_policy = p.insurance_policy;



-- RESULTADO FINAL

-- vehicles
-- owners
-- insurance_policies
-- ownership