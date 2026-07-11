from pydantic import BaseModel

class UserCreationRequest(BaseModel):
  username: str
  password: str
  phone_number: str

class UserCreationResponse(BaseModel):
  success: bool = True
  username: str | None = None

class UserAuthRequest(BaseModel):
  username: str
  password: str

class UserAuthResponse(BaseModel):
  success: bool
  username: str | None = None
  access_token: str | None = None

