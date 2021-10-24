#!/usr/bin/python3
"""Script to create an instance of the class user"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


association_table = Table("user_games", Base.metadata,
                          Column("user_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
                          Column("game_id", String(60), ForeignKey("game.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False))

association_table2 = Table("user_matches", Base.metadata,
                           Column("user_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
                           Column("match_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False))

association_table3 = Table("user_likes", Base.metadata,
                           Column("user_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
                           Column("like_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False))

association_table4 = Table("user_socials", Base.metadata,
                           Column("user_id", String(60), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
                           Column("social_id", String(60), ForeignKey("social.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
                           Column("link", String(50), nullable=False))

class User(BaseModel, Base):
    """Class to store the user data"""

    __tablename__ = "user"
    email = Column(String(30), nullable=False)
    nickname = Column(String(16), nullable=False)
    password = Column(String(15), nullable=False)
    bio = Column(String(300), nullable=True)
    games = relationship("Game", secondary="user_games", viewonly=False)
    matches = relationship("User", secondary="user_matches", primaryjoin="User.id==user_matches.c.user_id", secondaryjoin="User.id==user_matches.c.match_id", viewonly=False)
    likes = relationship("User", secondary="user_likes", primaryjoin="User.id==user_likes.c.user_id", secondaryjoin="User.id==user_likes.c.like_id", viewonly=False)
    socials = relationship("Socials", secondary="user_socials", viewonly=False)
