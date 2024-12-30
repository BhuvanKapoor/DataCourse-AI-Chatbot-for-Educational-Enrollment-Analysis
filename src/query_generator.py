import mysql.connector
from .logger import logger


def read_sql_query(query, db_config):
    logger.info("Executing SQL query: %s", query)
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
        )
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        logger.info("SQL query executed successfully, retrieved %d rows", len(rows))
        return rows
    except mysql.connector.Error as e:
        logger.error("Error executing SQL query: %s", str(e))
        return []
