from sqlalchemy.orm import Session
from src.models import models
from src.schemas import schemas

def create_user_input(db: Session, user_input: schemas.UserInputCreate):
    """
    Create a new entry in the database for the user's input and the generated result list.

    Args:
        db (Session): The database session.
        user_input (schemas.UserInputCreate): The schema containing the user's input.

    Returns:
        models.UserInput: The created database entry.
    """
    db_user_input = models.UserInput(
        identifier=user_input.identifier,
        result_list=user_input.result_list
    )
    db.add(db_user_input)
    db.commit()
    db.refresh(db_user_input)
    return db_user_input

def get_user_input_by_id(db: Session, user_input_id: int):
    """
    Retrieve a user input entry by its ID.

    Args:
        db (Session): The database session.
        user_input_id (int): The ID of the user input entry.

    Returns:
        models.UserInput: The retrieved database entry or None if not found.
    """
    return db.query(models.UserInput).filter(models.UserInput.id == user_input_id).first()

def get_all_user_inputs(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve all user input entries from the database.

    Args:
        db (Session): The database session.
        skip (int): Number of entries to skip.
        limit (int): Maximum number of entries to retrieve.

    Returns:
        List[models.UserInput]: A list of user input entries.
    """
    return db.query(models.UserInput).offset(skip).limit(limit).all()
