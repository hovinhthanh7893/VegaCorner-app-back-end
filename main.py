# Import FastAPI
from fastapi import FastAPI

# Initialize the app
app = FastAPI()

# Create endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

