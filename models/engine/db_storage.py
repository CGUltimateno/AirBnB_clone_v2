#!/usr/bin/python3
"""
Module for the DBStorage class
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    The DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        The init method of the DBStorage class
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        The all method of the DBStorage class
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Review).all())
        else:
            objs = self.__session.query(cls).all()

        dict = {}
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dict[key] = obj

        return dict

    def new(self, obj):
        """
        The new method of the DBStorage class
        """
        self.__session.add(obj)

    def save(self):
        """
        The save method of the DBStorage class
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        The delete method of the DBStorage class
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        The reload method of the DBStorage class
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        The close method of the DBStorage class
        """
        self.__session.close()