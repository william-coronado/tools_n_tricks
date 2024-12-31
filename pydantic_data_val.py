from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class User(BaseModel):
    username: str
    email: EmailStr
    age: int
    tags: List[str] = []
    profile: Optional[dict] = None

    @validator('age')
    def validate_age(cls, v):
        if v < 0:
            raise ValueError('Age must be positive')
        return v

# This will work
user = User(
    username="johndoe",
    email="john@example.com",
    age=25
)

# This will raise a validation error
user = User(
    username="johndoe",
    email="invalid-email",
    age=-5
)