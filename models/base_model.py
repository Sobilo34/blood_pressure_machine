#!/bin/usr/python3
"""
The base model that other models inherit from
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Sequence
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """
    The base model that other models inherit from
    """
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize the base model
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if not self.id:
            self.id = None
        if not self.created_at:
            self.created_at = datetime.utcnow()
        if not self.updated_at:
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Save the model to the database
        """
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """
        Delete the model from the database
        """
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """
        Return a dictionary representation of the model
        """
        model_dict = self.__dict__.copy()
        model_dict.pop('_sa_instance_state', None)
        return model_dict
