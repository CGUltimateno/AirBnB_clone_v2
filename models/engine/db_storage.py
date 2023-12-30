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
        url = f"mysql://{misc.user}:{misc.pwd}@{misc.host}/{misc.db}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if misc.ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current db session all cls objects
        this method must return a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        """
        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct

    def new(self, obj):
        """adds the obj to the current db session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current databse session the obj
            is it's not None
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """reloads the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
