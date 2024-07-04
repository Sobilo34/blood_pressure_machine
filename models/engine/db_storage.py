#!/usr/bin/python3

"""
This is the DBStorage class for Blood pressure machine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv
# from models.user import User
from models.bp import BloodPressureReading

classes = {
    'BloodPressureReading': BloodPressureReading
}

class DBStorage:
    __engine = None
    __session = None


    def __init__(self):
        """Instantiate a DBStorage object"""
        BP_MYSQL_USER = getenv('BP_MYSQL_USER')
        BP_MYSQL_PWD = getenv('BP_MYSQL_PWD')
        BP_MYSQL_HOST = getenv('BP_MYSQL_HOST')
        BP_MYSQL_DB = getenv('BP_MYSQL_DB')
        BP_ENV = getenv('BP_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(BP_MYSQL_USER,
                                             BP_MYSQL_PWD,
                                             BP_MYSQL_HOST,
                                             BP_MYSQL_DB))
        if BP_ENV == "test":
            Base.metadata.drop_all(self.__engine)
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
