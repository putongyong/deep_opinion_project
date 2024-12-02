from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src.entities import UserInputEntities
from src.crud import crud
from src.db.session import get_db

# Define a blueprint
bp = Blueprint('controllers', __name__)

@bp.route("/user_inputs/", methods=["POST"])
def create_user_input():
    """
    Endpoint to create a new user input and generate the result list.
    """
    db: Session = next(get_db())
    data = request.json

    try:
        user_input = UserInputEntities.UserInputCreate(**data)
        db_user_input = crud.create_user_input(db, user_input)
        return jsonify(UserInputEntities.UserInputResponse.model_dump(db_user_input)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

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
