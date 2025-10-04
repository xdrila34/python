import sqlite3
import os
from multiprocessing.connection import Connection

from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    connection = sqlite.connect(DATABASE_URL)
    Connection.row_factory = sqlite3.Row
    return connection