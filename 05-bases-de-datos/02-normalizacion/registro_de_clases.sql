-- PASO 0 - TABLA SIN NORMALIZAR

-- Problemas:
-- - Datos repetidos
-- - Difícil mantenimiento

CREATE TABLE student_data_unnormalized (
    student_id INTEGER,
    student_name TEXT,

    course_code TEXT,
    course_name TEXT,

    instructor_name TEXT,
    instructor_email TEXT
);


INSERT INTO student_data_unnormalized VALUES
(301, 'Marco Gómez', 'CS101', 'Python I', 'Juan Pérez', 'juan@uni.edu'),

(301, 'Marco Gómez', 'CS102', 'Python II', 'Laura Rojas', 'laura@uni.edu'),

(302, 'Carla Ruiz', 'CS101', 'Python I', 'Juan Pérez', 'juan@uni.edu');



-- PASO 1 - PRIMERA FORMA NORMAL (1NF)

-- PK:
-- (student_id, course_code)

CREATE TABLE student_data_1nf (
    student_id INTEGER,
    course_code TEXT,

    student_name TEXT,

    course_name TEXT,

    instructor_name TEXT,
    instructor_email TEXT,

    PRIMARY KEY (student_id, course_code)
);


INSERT INTO student_data_1nf (
    student_id,
    course_code,
    student_name,
    course_name,
    instructor_name,
    instructor_email
)
SELECT
    student_id,
    course_code,
    student_name,
    course_name,
    instructor_name,
    instructor_email
FROM student_data_unnormalized;



-- Problema:
-- student_id → estudiante
-- course_code → curso



-- PASO 2 - SEGUNDA FORMA NORMAL (2NF)

-- Separar:
-- - Students
-- - Courses
-- - Enrollments



-- STUDENTS_2NF

CREATE TABLE students_2nf (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT
);


INSERT INTO students_2nf (
    student_id,
    student_name
)
SELECT DISTINCT
    student_id,
    student_name
FROM student_data_1nf;



-- COURSES_2NF

CREATE TABLE courses_2nf (
    course_code TEXT PRIMARY KEY,
    course_name TEXT,

    instructor_name TEXT,
    instructor_email TEXT
);


INSERT INTO courses_2nf (
    course_code,
    course_name,
    instructor_name,
    instructor_email
)
SELECT DISTINCT
    course_code,
    course_name,
    instructor_name,
    instructor_email
FROM student_data_1nf;



-- ENROLLMENTS_2NF

CREATE TABLE enrollments_2nf (
    student_id INTEGER,
    course_code TEXT,

    PRIMARY KEY (student_id, course_code),

    FOREIGN KEY (student_id)
        REFERENCES students_2nf(student_id),

    FOREIGN KEY (course_code)
        REFERENCES courses_2nf(course_code)
);


INSERT INTO enrollments_2nf (
    student_id,
    course_code
)
SELECT
    student_id,
    course_code
FROM student_data_1nf;



-- Problema:
-- instructor_name → instructor_email
--
-- Dependencia transitiva



-- PASO 3 - TERCERA FORMA NORMAL (3NF)

-- Separar instructors



-- INSTRUCTORS

CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY AUTOINCREMENT,

    instructor_name TEXT,
    instructor_email TEXT
);


INSERT INTO instructors (
    instructor_name,
    instructor_email
)
SELECT DISTINCT
    instructor_name,
    instructor_email
FROM courses_2nf;



-- STUDENTS FINAL

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT
);


INSERT INTO students (
    student_id,
    student_name
)
SELECT
    student_id,
    student_name
FROM students_2nf;



-- COURSES FINAL

CREATE TABLE courses (
    course_code TEXT PRIMARY KEY,

    course_name TEXT,

    instructor_id INTEGER,

    FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
);


INSERT INTO courses (
    course_code,
    course_name,
    instructor_id
)
SELECT
    c.course_code,
    c.course_name,
    i.instructor_id
FROM courses_2nf c
JOIN instructors i
    ON c.instructor_name = i.instructor_name
   AND c.instructor_email = i.instructor_email;



-- ENROLLMENTS FINAL

CREATE TABLE enrollments (
    student_id INTEGER,
    course_code TEXT,

    PRIMARY KEY (student_id, course_code),

    FOREIGN KEY (student_id)
        REFERENCES students(student_id),

    FOREIGN KEY (course_code)
        REFERENCES courses(course_code)
);


INSERT INTO enrollments (
    student_id,
    course_code
)
SELECT
    student_id,
    course_code
FROM enrollments_2nf;



-- RESULTADO FINAL

-- instructors
-- students
-- courses
-- enrollments