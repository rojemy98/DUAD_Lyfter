-- PASO 0 - TABLA SIN NORMALIZAR

-- Problemas:
-- - Datos repetidos
-- - Dificil mantenimiento

CREATE TABLE employee_data_unnormalized (
    employee_id INTEGER,
    employee_name TEXT,

    department TEXT,
    department_phone TEXT,

    project_id TEXT,
    project_name TEXT,
    project_budget REAL
);


INSERT INTO employee_data_unnormalized VALUES
(201, 'Ana Rivera', 'IT', '2222-2222', 'P001', 'Web App', 50000),

(201, 'Ana Rivera', 'IT', '2222-2222', 'P002', 'API REST', 25000),

(202, 'Luis Mendez', 'Marketing', '1111-1111', 'P003', 'Campaña TV', 30000);



-- PASO 1 - PRIMERA FORMA NORMAL (1NF)

-- PK:
-- (employee_id, project_id)

CREATE TABLE employee_data_1nf (
    employee_id INTEGER,
    project_id TEXT,

    employee_name TEXT,

    department TEXT,
    department_phone TEXT,

    project_name TEXT,
    project_budget REAL,

    PRIMARY KEY (employee_id, project_id)
);


INSERT INTO employee_data_1nf (
    employee_id,
    project_id,
    employee_name,
    department,
    department_phone,
    project_name,
    project_budget
)
SELECT
    employee_id,
    project_id,
    employee_name,
    department,
    department_phone,
    project_name,
    project_budget
FROM employee_data_unnormalized;



-- Problema:
-- employee_id → empleado
-- project_id → proyecto



-- PASO 2 - SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- - Employees
-- - Projects
-- - EmployeeProjects



-- EMPLOYEES_2NF

CREATE TABLE employees_2nf (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT,
    department_phone TEXT
);


INSERT INTO employees_2nf (
    employee_id,
    employee_name,
    department,
    department_phone
)
SELECT DISTINCT
    employee_id,
    employee_name,
    department,
    department_phone
FROM employee_data_1nf;



-- PROJECTS_2NF

CREATE TABLE projects_2nf (
    project_id TEXT PRIMARY KEY,
    project_name TEXT,
    project_budget REAL
);


INSERT INTO projects_2nf (
    project_id,
    project_name,
    project_budget
)
SELECT DISTINCT
    project_id,
    project_name,
    project_budget
FROM employee_data_1nf;



-- EMPLOYEE_PROJECTS_2NF

CREATE TABLE employee_projects_2nf (
    employee_id INTEGER,
    project_id TEXT,

    PRIMARY KEY (employee_id, project_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees_2nf(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects_2nf(project_id)
);


INSERT INTO employee_projects_2nf (
    employee_id,
    project_id
)
SELECT
    employee_id,
    project_id
FROM employee_data_1nf;



-- Problema:
-- department → department_phone
--
-- Dependencia transitiva



-- PASO 3 - TERCERA FORMA NORMAL (3NF)

-- Separar departments



-- DEPARTMENTS

CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,

    department TEXT,
    department_phone TEXT
);


INSERT INTO departments (
    department,
    department_phone
)
SELECT DISTINCT
    department,
    department_phone
FROM employees_2nf;



-- EMPLOYEES FINAL

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,

    employee_name TEXT,

    department_id INTEGER,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


INSERT INTO employees (
    employee_id,
    employee_name,
    department_id
)
SELECT
    e.employee_id,
    e.employee_name,
    d.department_id
FROM employees_2nf e
JOIN departments d
    ON e.department = d.department
   AND e.department_phone = d.department_phone;



-- PROJECTS FINAL

CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    project_name TEXT,
    project_budget REAL
);


INSERT INTO projects (
    project_id,
    project_name,
    project_budget
)
SELECT
    project_id,
    project_name,
    project_budget
FROM projects_2nf;



-- EMPLOYEE_PROJECTS FINAL

CREATE TABLE employee_projects (
    employee_id INTEGER,
    project_id TEXT,

    PRIMARY KEY (employee_id, project_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);


INSERT INTO employee_projects (
    employee_id,
    project_id
)
SELECT
    employee_id,
    project_id
FROM employee_projects_2nf;



-- RESULTADO FINAL

-- departments
-- employees
-- projects
-- employee_projects