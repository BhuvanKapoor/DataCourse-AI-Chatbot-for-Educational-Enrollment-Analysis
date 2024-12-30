import random
import mysql.connector
from faker import Faker
from config.config import db_config
from src.logger import logger

# Connect to the MySQL database
logger.info("Connecting to the database for data insertion.")
connection = mysql.connector.connect(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"],
)
cursor = connection.cursor()

# Initialize Faker for random names
fake = Faker()

# Departments and courses data
departments = [
    {"dep_id": 1, "dep_name": "Data Science"},
    {"dep_id": 2, "dep_name": "Physics"},
    {"dep_id": 3, "dep_name": "Chemistry"},
]

courses = (
    [
        {
            "dep_id": 1,
            "course_name": f"DS Course {i+1}",
            "credits": random.randint(2, 5),
        }
        for i in range(12)
    ]
    + [
        {
            "dep_id": 2,
            "course_name": f"Physics Course {i+1}",
            "credits": random.randint(2, 5),
        }
        for i in range(12)
    ]
    + [
        {
            "dep_id": 3,
            "course_name": f"Chemistry Course {i+1}",
            "credits": random.randint(2, 5),
        }
        for i in range(12)
    ]
)

# Insert departments
logger.info("Started: Inserting departments into the database.")
for dep in departments:
    cursor.execute(
        "INSERT INTO department (dep_id, dep_name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE dep_name=dep_name",
        (dep["dep_id"], dep["dep_name"]),
    )
logger.info("Finished: Inserting departments into the database.")

# Insert courses
logger.info("Started: Inserting courses into the database.")
course_codes = []
for i, course in enumerate(courses):
    course_code = f"C{i+1:03}"
    course_codes.append((course_code, course["dep_id"]))
    cursor.execute(
        "INSERT INTO courses (course_code, course_name, dep_id, credits) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE course_name=course_name",
        (course_code, course["course_name"], course["dep_id"], course["credits"]),
    )
logger.info("Finished: Inserting courses into the database.")

# Insert students
logger.info("Started: Inserting students into the database.")
student_id_counter = {}
for year in range(2019, 2025):
    for course_code, dep_id in course_codes:
        num_students = random.randint(20, 30)
        for i in range(num_students):
            student_serial = student_id_counter.get(year, 1)
            student_id = int(f"{year % 100}{student_serial:03}")
            student_name = fake.name()
            cursor.execute(
                """
                INSERT INTO students (student_id, student_name, course_code, year_of_enrollment)
                VALUES (%s, %s, %s, %s)
                """,
                (student_id, student_name, course_code, year),
            )
            student_id_counter[year] = student_serial + 1
logger.info("Finished: Inserting students into the database.")

# Commit and close the connection
connection.commit()
cursor.close()
connection.close()

logger.info("Data insertion completed successfully.")
