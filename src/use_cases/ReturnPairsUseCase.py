from src.entities import UserInputEntities

def return_pairs(input_data: UserInputEntities.RangeInput) -> UserInputEntities.UserInputBase:
    """
    Generate a UserInputBase object containing an identifier and a list of even numbers 
    within a specified range.

    Args:
        input_data (RangeInput): A schema object containing:
                                 - id (str): A unique identifier.
                                 - int1 (int): One boundary of the range (inclusive).
                                 - int2 (int): The other boundary of the range (inclusive).

    Returns:
        UserInputBase: A schema object with:
                       - identifier (str): The provided identifier.
                       - result_list (List[int]): A list of even integers within the 
                                                  inclusive range [min(int1, int2), max(int1, int2)].
    """
    # Determine the range boundaries
    left, right = sorted((input_data.int1, input_data.int2))
    
    # Generate the list of even numbers using list comprehension
    pairs_list = [i for i in range(left, right + 1) if i % 2 == 0]

    # Return a UserInputBase object
    return UserInputEntities.UserInputBase(
        identifier=input_data.id,
        result_list=pairs_list
    )
