from pydantic import BaseModel
from typing import List

class RangeInput(BaseModel):
    """
    Schema for range input with identifier and range bounds.
    """
    id: str
    int1: int
    int2: int

class UserInputBase(BaseModel):
    """
    Base schema for user input and generated results.
    """
    identifier: str
    result_list: List[int]

class UserInputCreate(UserInputBase):
    """
    Schema for creating a new user input entry.
    """
    pass

class UserInputResponse(UserInputBase):
    """
    Schema for returning a user input entry.
    """
    id: int  # Include ID in the response

    class Config:
        from_attributes = True  # Enable ORM mode for compatibility with SQLAlchemy models
