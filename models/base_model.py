#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

        if not kwargs:
            from models import storage
            id = Column(String(60), primary_key=True, nullable=False)
            created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
            updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        models.storage.new(self)
        models.storage.save()


    def to_dict(self):
        base_dict = {key: val for key, val in self.__dict__.items() if key != '_sa_instance_state'}
        return {**base_dict, **{'__class__': self.__class__.__name__}}

    def delete(self):
        models.storage.delete(self)
