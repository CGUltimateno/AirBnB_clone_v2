#!/usr/bin/python3
"""file system"""
from sqlalchemy.orm import scoped_session, sessionmaker

import models.misc as misc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """A class for the DB storage system"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializing instance"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                misc.user, misc.pwd, misc.host, misc.db
            ),
            pool_pre_ping=True,
        )

        if misc.ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns objects from db"""
        all_objs = {}

        if cls:
            objects = self.__session.query(cls)
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                all_objs[key] = obj
        else:
            for item in misc.classes.values():
                objects = self.__session.query(item)
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """adds new obj to session"""
        self.__session.add(obj)

    def save(self):
        """save session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload db"""
        Base.metadata.create_all(self.__engine)
        session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = scoped_session(session)

    def close(self):
        """close"""
        self.__session.close()
