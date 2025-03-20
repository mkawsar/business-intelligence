from fastapi import FastAPI
from src.config.settings import settings
from src.config.database import startDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """
    Event handler for the FastAPI application startup event.
    Initializes the database connection using the startDB function.
    """

    await startDB()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}

