# Import FastAPI
from fastapi import FastAPI

# Create app
app = FastAPI()

# Create end-point
@app.get("/")
async def root():
    return {"message": "Hello World"}

