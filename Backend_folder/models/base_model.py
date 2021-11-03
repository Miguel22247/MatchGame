#!/usr/bin/python3.6
"""Base model for all objects"""
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from uuid import uuid4


Base = declarative_base()


class BaseModel:
    """Base model class for methods of all classes"""

    id = Column(String(60), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        """Initialization function"""
        self.id = str(uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """Adds the object to the storages and saves it"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """Deletes the object from storage"""
        models.storage.delete(self)
