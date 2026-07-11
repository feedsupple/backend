from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = getenv("DATABASE_URL", None)
engine = create_engine(
  DATABASE_URL,
  echo=False,
  pool_pre_ping=True,
)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False,
  autocommit=False,
)

def get_session_generator():
  session = SessionLocal()

  try:
    yield session
  finally:
    session.close()

def get_session():
  return next(get_session_generator())

class Base(DeclarativeBase):
  pass

