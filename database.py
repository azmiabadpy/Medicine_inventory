import pymysql
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def get_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection
