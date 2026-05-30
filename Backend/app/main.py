from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.occupancy import router as occupancy_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(occupancy_router)

@app.get("/")
def home():
    return {"message": "Crowd Control backend running"}