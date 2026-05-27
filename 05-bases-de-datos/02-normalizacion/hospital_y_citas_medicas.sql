-- PASO 0 - TABLA SIN NORMALIZAR

-- Problemas:
-- - Datos repetidos
-- - Difícil mantenimiento

CREATE TABLE appointment_data_unnormalized (
    appointment_id TEXT,

    patient_name TEXT,
    patient_phone TEXT,

    doctor_name TEXT,
    specialty TEXT,

    appointment_date TEXT,
    appointment_time TEXT
);


INSERT INTO appointment_data_unnormalized VALUES
('A01', 'Diana Vargas', '8888-1111', 'Dr. Soto', 'Pediatría', '2024-08-01', '10:00 AM'),

('A02', 'Diana Vargas', '8888-1111', 'Dr. Soto', 'Pediatría', '2024-08-10', '10:00 AM'),

('A03', 'Edwin Mora', '8999-2222', 'Dr. Mora', 'Cardiología', '2024-08-05', '01:00 PM');



-- PASO 1 - PRIMERA FORMA NORMAL (1NF)

-- PK:
-- appointment_id

CREATE TABLE appointment_data_1nf (
    appointment_id TEXT PRIMARY KEY,

    patient_name TEXT,
    patient_phone TEXT,

    doctor_name TEXT,
    specialty TEXT,

    appointment_date TEXT,
    appointment_time TEXT
);


INSERT INTO appointment_data_1nf (
    appointment_id,
    patient_name,
    patient_phone,
    doctor_name,
    specialty,
    appointment_date,
    appointment_time
)
SELECT
    appointment_id,
    patient_name,
    patient_phone,
    doctor_name,
    specialty,
    appointment_date,
    appointment_time
FROM appointment_data_unnormalized;



-- Problema:
-- patient_phone → paciente
-- doctor_name → specialty



-- PASO 2 - SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- - Patients
-- - Doctors
-- - Appointments



-- PATIENTS_2NF

CREATE TABLE patients_2nf (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,
    patient_phone TEXT
);


INSERT INTO patients_2nf (
    patient_name,
    patient_phone
)
SELECT DISTINCT
    patient_name,
    patient_phone
FROM appointment_data_1nf;



-- DOCTORS_2NF

CREATE TABLE doctors_2nf (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,

    doctor_name TEXT,
    specialty TEXT
);


INSERT INTO doctors_2nf (
    doctor_name,
    specialty
)
SELECT DISTINCT
    doctor_name,
    specialty
FROM appointment_data_1nf;



-- APPOINTMENTS_2NF

CREATE TABLE appointments_2nf (
    appointment_id TEXT PRIMARY KEY,

    patient_id INTEGER,
    doctor_id INTEGER,

    appointment_date TEXT,
    appointment_time TEXT,

    FOREIGN KEY (patient_id)
        REFERENCES patients_2nf(patient_id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctors_2nf(doctor_id)
);


INSERT INTO appointments_2nf (
    appointment_id,
    patient_id,
    doctor_id,
    appointment_date,
    appointment_time
)
SELECT
    a.appointment_id,
    p.patient_id,
    d.doctor_id,
    a.appointment_date,
    a.appointment_time
FROM appointment_data_1nf a
JOIN patients_2nf p
    ON a.patient_phone = p.patient_phone
JOIN doctors_2nf d
    ON a.doctor_name = d.doctor_name;



-- Problema:
-- specialty puede repetirse
--
-- Dependencia transitiva



-- PASO 3 - TERCERA FORMA NORMAL (3NF)

-- Separar specialties



-- SPECIALTIES

CREATE TABLE specialties (
    specialty_id INTEGER PRIMARY KEY AUTOINCREMENT,

    specialty_name TEXT
);


INSERT INTO specialties (
    specialty_name
)
SELECT DISTINCT
    specialty
FROM doctors_2nf;



-- DOCTORS FINAL

CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY,

    doctor_name TEXT,

    specialty_id INTEGER,

    FOREIGN KEY (specialty_id)
        REFERENCES specialties(specialty_id)
);


INSERT INTO doctors (
    doctor_id,
    doctor_name,
    specialty_id
)
SELECT
    d.doctor_id,
    d.doctor_name,
    s.specialty_id
FROM doctors_2nf d
JOIN specialties s
    ON d.specialty = s.specialty_name;



-- PATIENTS FINAL

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    patient_phone TEXT
);


INSERT INTO patients (
    patient_id,
    patient_name,
    patient_phone
)
SELECT
    patient_id,
    patient_name,
    patient_phone
FROM patients_2nf;



-- APPOINTMENTS FINAL

CREATE TABLE appointments (
    appointment_id TEXT PRIMARY KEY,

    patient_id INTEGER,
    doctor_id INTEGER,

    appointment_date TEXT,
    appointment_time TEXT,

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id)
);


INSERT INTO appointments (
    appointment_id,
    patient_id,
    doctor_id,
    appointment_date,
    appointment_time
)
SELECT
    appointment_id,
    patient_id,
    doctor_id,
    appointment_date,
    appointment_time
FROM appointments_2nf;



-- RESULTADO FINAL

-- specialties
-- doctors
-- patients
-- appointments