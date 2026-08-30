from pydantic import BaseModel
from typing import List

class Shoe(BaseModel):
    gender: str
    shoe_type: str
    color: str
    price: float
    manufacturer: str
    size: int

class Recipe(BaseModel):
    name: str
    author: str
    recipe_type: str
    description: str
    video_link: str
    ingredients: List[str]
    cuisine: str