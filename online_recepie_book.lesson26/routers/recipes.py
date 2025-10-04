from fastapi import APIRouter, HTTPException
from typing import List
from models.recipe import Recipe, RecipeCreate
from database import get_db_connection

router = APIRouter()

def category_exists(category_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM categories WHERE id = ?", (category_id,))
    results = cursor.fetchone()
    conn.close()
    return results is not None

@router.get(path="/recipes/", response_model=List[Recipe])
def get_recipes(cuisine: str = None, difficulty: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM recipes WHERE 1 = 1"
    params = []

    if cuisine:
        query += " AND cuisine = ?"
        params.append(cuisine)
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)

    cursor.execute(query, params)
    recipes = cursor.fetchall()
    conn.close()

    return [
        Recipe(
            id=row[0],
            name=row[1],
            description=row[2],
            ingredients=row[3],
            instruction=row[4],
            cuisine=row[5],
            difficulty=row[6],
            category_id=row[7]
        )
        for row in recipes
    ]
@router.delete(path="/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Recipe not found")
    conn.commit()
    conn.close()
    return {"details": "Recipe deleted"}

