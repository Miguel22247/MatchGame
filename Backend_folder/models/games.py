#!/usr/bin/python3
"""Script to create an instance of the class game"""
from sqlalchemy import Column, String
from models import storage
from models.base_model import Base, BaseModel


class Game(BaseModel, Base):
    """Class to store the game data"""

    __tablename__ = "games"
    name = Column(String(50), nullable=False)
