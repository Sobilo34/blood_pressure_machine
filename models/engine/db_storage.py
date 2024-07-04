#!/usr/bin/python3

"""
This is the DBStorage class for Blood pressure machine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.bp import Bp

classes = {
    'User': User,
    'BloodPressureReading': BloodPressureReading
}

class DBStorage:
    __engine = None
    __session = None


    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://bp_user:bp_pwd@localhost/bp_db')
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        if cls is None:
            return self.__session.query(User).all() + self.__session.query(Bp).all()
        else:
            return self.__session.query(cls).all()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
