from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Recipe(BaseModel):
    name: str
    ingredient: str

inventory = {
    1: {
        "name": "Tofu",
        "ingredient": "Soy bean"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/recipe_id/{id}")
def get_item(id: int):
    return inventory[id]

@app.get("/recipe_name/{name}")
def get_item(name: str):
    for id in inventory:
        if inventory[id]["name"] == name:
            return inventory[id]
    return {"Data": "Not found"}

@app.post("/create_recipe")
def create_item(recipe: Recipe):
    inventory[len(inventory) + 1] = {"name": recipe.name, "ingredient": recipe.ingredient}
    return inventory[len(inventory) + 1] 