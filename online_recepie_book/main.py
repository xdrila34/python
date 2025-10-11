from fastapi import FastAPI
from routers import recipes,categories
import os
from dotenv import load_dotenv
from database import get_d_connection

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

app.include_router(categories.router)
app.include_router(recipes.router)

@app.on_event('startup')
def start_up():
    conn = get_db_connecion()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
            )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recepies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT  NOT NULL,
            description TEXT,
            ingredients TEXT,
            instructions TEXT,
            cuisine TEXT,
            difficulty TEXT,
            category_id INTEGER,
            FOREIGN KEY (caegory_id) REFERENCES categories (id) 
            )
        ''')
    conn.commit()
    conn.close()
@app.get('/')
def reaad_root():
    return{"message": "FastAPI with SQLite project"}