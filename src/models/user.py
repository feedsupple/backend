from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import Base

class User(Base):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(
    primary_key=True, autoincrement=True
  )

  username: Mapped[str] = mapped_column(
    String(100), unique=True, nullable=False
  )

  phone_number: Mapped[str] = mapped_column(
    String(20), unique=True, nullable=False
  )

  password_hash: Mapped[str] = mapped_column(
    String(255), nullable=False
  )

