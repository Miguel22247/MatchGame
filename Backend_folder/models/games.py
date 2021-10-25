#!/usr/bin/python3
"""Script to create an instance of the class game"""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class Game(BaseModel, Base):
    """Class to store the game data"""

    __tablename__ = "game"
    name = Column(String(50), nullable=False)
