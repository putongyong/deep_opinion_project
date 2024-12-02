from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserInput(Base):
    """
    This is a model extending the SQLAlchemy Base.
    Its purpose is to create the database table for storing user input and results.
    """
    __tablename__ = "user_inputs"
    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    identifier = Column(String, nullable=False)  # User identifier
    result_list = Column(JSON, nullable=False)  # JSON field to store the generated list

    def __repr__(self):
        return f"<UserInput(identifier='{self.identifier}', result_list={self.result_list})>"
