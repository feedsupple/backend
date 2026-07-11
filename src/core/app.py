from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text

from src.core.db import engine
from src.routes.user import UserRouter

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(UserRouter.router)

@app.get("/")
def app_root():
  return "Hello, FeedSupple Backend!"

@app.get("/health")
def health_check():
  api_healthy = True
  db_healthy = True

  with engine.connect() as connection:
    try:
      connection.execute(text("SELECT 1"))
    except Exception as e:
      db_healthy = False

  return {
    "api": api_healthy,
    "db": db_healthy,
  }

