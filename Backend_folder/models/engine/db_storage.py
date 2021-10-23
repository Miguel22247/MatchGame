#!/usr/bin/python3
"""Engine to manipulate the storage in the database"""
from models.base_model import Base, BaseModel
from models.games import Game
from models.user import User
from models.socials import Social
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

class DBStorage:
    """A database storage engine"""


    __engine = None
    __session = None
    __class_list = {"User": User, "Game": Game, "Social": Social}
    __user = getenv("DB_USER")
    __pwd = getenv("DB_PSW")
    __host = getenv("DB_HOST")
    __db = getenv("GM_DB")


    def __init__(self):
        """Initializes a new dbstorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(self.__user, self.__pwd,
                                             self.__host, self.__db),
                                             pool_pre_ping=True)

    def all(self, cls=None):
        """turns a list with all objects. If a class is given
        only returns objects of that class"""
        objs_dict = {}
        for clss in self.__class_list:
            if cls is None or cls is self.__class_list[clss] or cls is clss:
                objs = self.__session.query(self.__class_list[clss]).all()
                for obj in objs:
                    key = obj.id
                    objs_dict[key] = obj
        return (objs_dict)

    def new(self, obj):
        """Add an object to the databse"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database
        and initializes a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current SQLAlchemy session"""
        self.__session.close()

    def get(self, cls, id):
        """Returns an object based on the id and class"""
        all_dict = self.all(cls)
        if id in all_dict:
            return(all_dict[id])
        else:
            return None
