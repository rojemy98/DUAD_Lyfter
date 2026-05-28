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

-- make --> model

-- insurance_policy --> insurance_company



-- SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- Vehicles
-- Owners
-- Insurance
-- Ownership



-- VEHICLE_MODELS_2NF

-- model depende de make

CREATE TABLE vehicle_models_2nf (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,

    make TEXT,
    model TEXT
);


INSERT INTO vehicle_models_2nf (
    make,
    model
)
SELECT DISTINCT
    make,
    model
FROM vehicle_data_1nf;



-- VEHICLES_2NF

CREATE TABLE vehicles_2nf (
    vin TEXT PRIMARY KEY,

    model_id INTEGER,

    year INTEGER,
    color TEXT,

    FOREIGN KEY (model_id)
        REFERENCES vehicle_models_2nf(model_id)
);


INSERT INTO vehicles_2nf (
    vin,
    model_id,
    year,
    color
)
SELECT DISTINCT
    v.vin,
    m.model_id,
    v.year,
    v.color
FROM vehicle_data_1nf v
JOIN vehicle_models_2nf m
    ON v.make = m.make
   AND v.model = m.model;



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



-- INSURANCE_COMPANIES_2NF

CREATE TABLE insurance_companies_2nf (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_name TEXT
);


INSERT INTO insurance_companies_2nf (
    company_name
)
SELECT DISTINCT
    insurance_company
FROM vehicle_data_1nf;



-- INSURANCE_POLICIES_2NF

-- policy depende de company

CREATE TABLE insurance_policies_2nf (
    policy_id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_id INTEGER,

    policy_name TEXT,

    FOREIGN KEY (company_id)
        REFERENCES insurance_companies_2nf(company_id)
);


INSERT INTO insurance_policies_2nf (
    company_id,
    policy_name
)
SELECT DISTINCT
    c.company_id,
    v.insurance_policy
FROM vehicle_data_1nf v
JOIN insurance_companies_2nf c
    ON v.insurance_company = c.company_name;



-- OWNERSHIP_2NF

CREATE TABLE ownership_2nf (
    vin TEXT,
    owner_id INTEGER,
    policy_id INTEGER,

    PRIMARY KEY (vin, owner_id),

    FOREIGN KEY (vin)
        REFERENCES vehicles_2nf(vin),

    FOREIGN KEY (owner_id)
        REFERENCES owners_2nf(owner_id),

    FOREIGN KEY (policy_id)
        REFERENCES insurance_policies_2nf(policy_id)
);


INSERT INTO ownership_2nf (
    vin,
    owner_id,
    policy_id
)
SELECT
    v.vin,
    v.owner_id,
    p.policy_id
FROM vehicle_data_1nf v
JOIN insurance_companies_2nf c
    ON v.insurance_company = c.company_name
JOIN insurance_policies_2nf p
    ON p.company_id = c.company_id
   AND p.policy_name = v.insurance_policy;



-- Problema:
-- make se repite
-- Dependencia transitiva



-- ERCERA FORMA NORMAL (3NF)

-- Separar makes



-- MAKES

CREATE TABLE makes (
    make_id INTEGER PRIMARY KEY AUTOINCREMENT,

    make_name TEXT
);


INSERT INTO makes (
    make_name
)
SELECT DISTINCT
    make
FROM vehicle_models_2nf;



-- VEHICLE_MODELS FINAL

CREATE TABLE vehicle_models (
    model_id INTEGER PRIMARY KEY,

    make_id INTEGER,

    model_name TEXT,

    FOREIGN KEY (make_id)
        REFERENCES makes(make_id)
);


INSERT INTO vehicle_models (
    model_id,
    make_id,
    model_name
)
SELECT
    vm.model_id,
    m.make_id,
    vm.model,
    vm.model
FROM vehicle_models_2nf vm
JOIN makes m
    ON vm.make = m.make_name;



-- VEHICLES FINAL

CREATE TABLE vehicles (
    vin TEXT PRIMARY KEY,

    model_id INTEGER,

    year INTEGER,
    color TEXT,

    FOREIGN KEY (model_id)
        REFERENCES vehicle_models(model_id)
);


INSERT INTO vehicles (
    vin,
    model_id,
    year,
    color
)
SELECT
    vin,
    model_id,
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



-- INSURANCE_COMPANIES FINAL

CREATE TABLE insurance_companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT
);


INSERT INTO insurance_companies (
    company_id,
    company_name
)
SELECT
    company_id,
    company_name
FROM insurance_companies_2nf;



-- INSURANCE_POLICIES FINAL

CREATE TABLE insurance_policies (
    policy_id INTEGER PRIMARY KEY,

    company_id INTEGER,

    policy_name TEXT,

    FOREIGN KEY (company_id)
        REFERENCES insurance_companies(company_id)
);


INSERT INTO insurance_policies (
    policy_id,
    company_id,
    policy_name
)
SELECT
    policy_id,
    company_id,
    policy_name
FROM insurance_policies_2nf;



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
    vin,
    owner_id,
    policy_id
FROM ownership_2nf;



-- RESULTADO FINAL

-- makes
-- vehicle_models
-- vehicles
-- owners
-- insurance_companies
-- insurance_policies
-- ownership