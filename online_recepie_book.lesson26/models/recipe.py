from pydantic import BaseModel
from typing import Optional

class RecipeBase(BaseModel):
    name: str
    description:Optional[str] = None
    ingredients: str
    instruction: str
    cuisine: str
    difficulty: str
    category_id: Optional[int] = None

class Recipe(BaseModel):
    id: int