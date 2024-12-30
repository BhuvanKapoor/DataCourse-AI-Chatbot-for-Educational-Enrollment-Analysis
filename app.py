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

prompt_response = [
    """
    You are a skilled data analyst tasked with interpreting information from a SQL database. Below is a combined string that includes a SQL query and its corresponding output: Query, Output
    Your task is to provide a clear and concise explanation of the output data in human language, incorporating the actual values from the output. Please include the following sections in your response:


    Highlight key insights or trends from the output, using the actual values to illustrate your points. For example, mention the names of the students and their respective years of enrollment.

    Ensure your explanation is straightforward and accessible, allowing anyone reading it to grasp the insights derived from the data.
    """
]

## Streamlit App

st.set_page_config(page_title="DataCourse")
st.header("DataCourse: AI Chatbot for Educational Enrollment Analysis")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    logger.info("User question submitted!!")
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, DB_CONFIG)
    question = f"Query: {response}\nOutput: {data}"
    output_response = get_gemini_response(question, prompt_response)
    # st.subheader("The Response is")
    st.write(output_response)
    logger.info("User question has been answered!!")
