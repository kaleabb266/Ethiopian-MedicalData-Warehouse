# dashboard/utils.py
import psycopg2
import pandas as pd


def get_data(query):
    """
    Fetch data from PostgreSQL database.
    """
    try:
        # Database connection parameters
        conn = psycopg2.connect(
            dbname="telegram_data",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()