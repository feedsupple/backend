from fastapi import APIRouter

from src.core.db import get_session
from src.models.user import User
from src.utils.hasher import SecretHasher

from src.schemas.user import (
  UserAuthRequest,
  UserAuthResponse,
  UserCreationRequest,
  UserCreationResponse,
)

user_router = APIRouter(prefix="/users", tags=["users"])

class UserRouter:
  router = user_router

post = user_router.post
get = user_router.get

@post("/", response_model=UserCreationResponse)
def create_user(requestDTO: UserCreationRequest):
  """
  Create a new user with the provided username, phone number, and password.
  """
  user = User(
    username=requestDTO.username,
    phone_number=requestDTO.phone_number,
    password_hash=SecretHasher.hash_secret(requestDTO.password),
  )

  try:
    session = get_session()
    session.add(user)
    session.commit()
    session.refresh(user)
  except Exception as e:
    session.rollback()
    print(f"Error creating user: {e}")

    return {
      "success": False,
      "username": None,
    }

  return {
    "success": True,
    "username": user.username,
  }

@post("/auth", response_model=UserAuthResponse)
def authenticate_user(requestDTO: UserAuthRequest):
  """
  Authenticate a user with the provided username and password.
  """
  session = get_session()
  user = session.query(User).filter_by(username=requestDTO.username).first()
  verified = user and SecretHasher.verify_hash(
    requestDTO.password,
    user.password_hash,
  )

  if not verified:
    return {
      "success": False,
      "username": None,
      "access_token": None,
    }

  return {
    "success": True,
    "username": user.username,
    "access_token": "dummy_access_token",
  }

