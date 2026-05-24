from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import venues

 
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(venues.router)

@app.get("/")
def home():
    return {"message": "Crowd Control Backend"}