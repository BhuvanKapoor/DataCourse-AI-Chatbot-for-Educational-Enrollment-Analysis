# DataCourse: AI Chatbot for Educational Enrollment Analysis

## Overview
This project is an AI-powered chatbot designed to provide descriptive analysis and visualizations based on user queries related to educational enrollment data. The chatbot interacts with a SQL database containing information about students, courses, and departments over the last five years.

## Features
- **Natural Language Processing**: Converts user queries into SQL commands.
- **Logging**: Logs all operations for debugging and monitoring purposes.
- **User-Friendly Interface**: Built with Streamlit.

## Technologies Used
- Python
- Streamlit
- MySQL
- Pandas
- Faker (for generating random data)
- Google Generative AI (for natural language processing)

## Project Structure
```
/Educational Enrollment Analysis Chatbot
│
├── /config
│    ├── __init__.py
│    └── config.py                # Configuration files
├── /data
│    └── schema.sql                  
├── /src                   # Source code for the application
│   ├── __init__.py
│   ├── data.py            # Data generation script
│   ├── logger.py          # Looging script
│   └── query_generator.py # Query generation script
│   
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Prerequisites
- Python 3.7 or higher
- MySQL Server
- Google API Key for Generative AI

## Installation Steps

### Clone the Repository
```bash
git clone https://github.com/BhuvanKapoor/DataCourse-AI-Chatbot-for-Educational-Enrollment-Analysis.git
cd DataCourse-AI-Chatbot-for-Educational-Enrollment-Analysis
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
GOOGLE_API_KEY=your_google_api_key
```

### Set Up MySQL Database
1. Create a MySQL database and tables as per the schema defined in the `data/schema.sql` file.
2. Run the `data.py` script to populate the database with sample data:
   ```bash
   python src/data.py
   ```

### Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```


## Usage
- Type your questions related to student enrollment, courses, or departments in the input field.
- The chatbot will process your query, execute the corresponding SQL command, and display the results.

## Logging
All operations are logged in `logs/app.log`. This includes user interactions, SQL query executions, and any errors encountered.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.