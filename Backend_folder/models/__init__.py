#!/usr/bin/python3.6
"""Initializates the storage for the database"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
