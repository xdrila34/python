import sqlite3
from typing import List
from streamlit import status
from models.category import Category, CategoryCreate
from database import get_db_connection
from fastapi import APIRouter, HTTPException
from unicodedata import category

from main import cursor

router = APIRouter()

@router.get(path="/categories/", response_model=List[Category])
def get_categories():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name from categories")
    categories = cursor.fetchall()
    conn.close()

    category_list = [{"id": cat[0], "name": cat[1]} for cat in categories]
    return category_list


@router.post(path="/categories/", response_model=Category)
def create_category(category: CategoryCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO categories(name) VALUES(?)", (category.name,))
        conn.commit()
        category_id = cursor.lastrowid
        return Category(id=category_id, name=category.name)
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The category '{category.name}', already exists."
        )
    except Exception as e:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SEVER_ERROR,
            detail=f"anerror occured: {e}"
        )
    finally:
        conn.close()

@router.put('/categorues/{category_id', response_model=Category)
def update_category(category_id: int, category: CategoryCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE categorues Set name = ? WHERE id = ?",(category.name,category_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="category not found")
    conn.commit()
    conn.close()
    return Category(id = category_id, name = category.name)

@router.delete("/categories/{category_id}", response_model=dict)
def delete_category(category_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="category not found")
    conn.commit()
    conn.close()
    return {"details": "Category Delteted"}


