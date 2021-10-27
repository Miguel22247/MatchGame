#!/usr/bin/python3
"""Script to create an instance of the class Social"""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class Social(BaseModel, Base):
    """Class to store the social data"""
    __tablename__ = "social"
    name = Column(String(20), nullable=False)
