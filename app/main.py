from fastapi import FastAPI
from app import config
from app.routers.routes import router as api_router


app = FastAPI()

app.include_router(api_router)  # Register all routes centrally

@app.get("/")
def root():
    return {
        "status": "ok",
        "mode": config.MODE,
        "database": config.DB_NAME
    }
