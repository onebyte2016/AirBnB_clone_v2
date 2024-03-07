import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models import *

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB'),
                                             pool_pre_ping=True),
                                      echo=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of objects depending on the class name.
        If cls is None, returns all types of objects.
        """
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        objects_dict = {}
        for class_ in classes:
            objects = self._session.query(class_).all()
        for obj in objects:
            key = "{}.{}".format(obj._class.name_, obj.id)
            objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """
        Adds the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session if it's not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and initializes the database session.
        """
        # Step 1: Import necessary modules and classes

        # Step 2: Create tables in the database
        Base.metadata.create_all(self.__engine)

        # Step 3: Create the current database session
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
