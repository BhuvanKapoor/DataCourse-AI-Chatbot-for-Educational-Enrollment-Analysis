from dotenv import load_dotenv
from src.query_generator import read_sql_query
import streamlit as st
import os
from config.config import DB_CONFIG
import google.generativeai as genai
from src.logger import logger

load_dotenv()  ## load all the environemnt variables


## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    logger.info("Fetching response from Gemini-pro model...")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    logger.info("Received response from Gemini-pro model...")
    return response.text


## Define Your Prompt
prompt = [
    """
        You are an expert in converting English questions to SQL queries!
        The SQL database has the following tables: department, courses, and students.

        The department table has the following columns: dep_id, dep_name.
        The courses table has the following columns: course_code, course_name, dep_id, credits.
        The students table has the following columns: student_id, student_name, course_code, year_of_enrollment.
        For example:

        Example 1 - How many students are enrolled in the Data Science department?
        The SQL command will be something like this:
        SELECT COUNT(*) AS Student_Count, s.year_of_enrollment FROM students AS s JOIN courses AS c ON s.course_code = c.course_code JOIN department AS d ON c.dep_id = d.dep_id WHERE d.dep_name = 'Data Science' GROUP BY s.year_of_enrollment;

        Example 2 - What are the names of the students enrolled in the course 'C001'?
        The SQL command will be something like this:
        SELECT student_name FROM students WHERE course_code = 'C001';

        Also, the SQL code should not have ``` in the beginning or end, and the word "SQL" should not be included in the output.
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    logger.info("User question submitted!!")
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, DB_CONFIG)
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
    logger.info("User question has been answered!!")
