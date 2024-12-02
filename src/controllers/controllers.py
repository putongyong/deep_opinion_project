from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src.entities import UserInputEntities
from src.crud import crud
from src.db.session import get_db
from src.use_cases import ReturnPairsUseCase
from pydantic import ValidationError

# Define a blueprint
bp = Blueprint('controllers', __name__)

@bp.route("/user_inputs/", methods=["POST"])
def create_user_input():
    """
    Endpoint to create a new user input and generate the result list.
    """
    db: Session = next(get_db())

    if not request.json:
        return jsonify({"error": "Empty payload"}), 400

    try:
        # Parse and validate JSON input with Pydantic
        input_data = UserInputEntities.RangeInput(**request.json)
        output_data: UserInputEntities.UserInputBase = ReturnPairsUseCase.return_pairs(input_data)
        # Create the user input in the database
        db_user_input = crud.create_user_input(db, output_data)
        
        # Convert ORM object to dictionary for Pydantic compatibility
        db_user_input_dict = db_user_input.__dict__
        
        # Use Pydantic to serialize the response
        response_data = UserInputEntities.UserInputResponse(**db_user_input_dict)
        return jsonify(response_data.model_dump()), 201
    except ValidationError as e:
        # Return detailed validation errors
        return jsonify({"error": "Validation failed", "details": e.errors()}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

@bp.route("/user_inputs/<int:user_input_id>", methods=["GET"])
def read_user_input(user_input_id: int):
    """
    Endpoint to fetch a specific user input by its ID.
    """
    db: Session = next(get_db())
    db_user_input = crud.get_user_input_by_id(db, user_input_id)

    if db_user_input is None:
        return jsonify({"error": "User input not found"}), 404

    return jsonify(UserInputEntities.UserInputResponse.model_dump(db_user_input)), 200

@bp.route("/all_user_inputs/", methods=["GET"])
def read_all_user_inputs():
    """
    Endpoint to fetch all user inputs with pagination.
    """
    db: Session = next(get_db())
    try:
        offset = int(request.args.get("offset", 0))  # Default offset to 0
        limit = int(request.args.get("limit", 10))   # Default limit to 10

        user_inputs = crud.get_all_user_inputs(db, skip=offset, limit=limit)
        return jsonify([UserInputEntities.UserInputResponse.model_dump(user_input) for user_input in user_inputs]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
