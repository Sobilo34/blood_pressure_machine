#!/usr/bin/pyhton3
"""
This is the model for User
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

engine = create_engine('mysql+mysqldb://bp_user:bp_pwd@localhost/bp_db')

Base = declarative_base()

class User(BaseModel, Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(100))

# Create tables
Base.metadata.create_all(engine)