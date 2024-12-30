-- Department table
CREATE TABLE department (
    dep_id INT PRIMARY KEY,
    dep_name VARCHAR(100) NOT NULL
);

-- Courses table with foreign key reference to department
CREATE TABLE courses (
    course_code VARCHAR(20) PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    dep_id INT NOT NULL,
    credits INT NOT NULL,
    FOREIGN KEY (dep_id) REFERENCES department(dep_id)
);

-- Students table with foreign key reference to courses
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) NOT NULL,
    year_of_enrollment INT NOT NULL,
    FOREIGN KEY (course_code) REFERENCES courses(course_code)
);

-- Adding indexes for better query performance
CREATE INDEX idx_department_name ON department(dep_name);
CREATE INDEX idx_course_name ON courses(course_name);
CREATE INDEX idx_student_name ON students(student_name);
CREATE INDEX idx_enrollment_year ON students(year_of_enrollment);