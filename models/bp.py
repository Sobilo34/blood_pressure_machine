#!/usr/bin/python3
"""
This is the model for Blood pressure machine
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Sequence
from models.base_model import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# engine = create_engine('mysql+mysqldb://bp_user:bp_pwd@localhost/bp_db')

Base = declarative_base()

class BloodPressureReading(BaseModel, Base):
    __tablename__ = 'blood_pressure_readings'
    id = Column(Integer, Sequence('bp_id_seq'), primary_key=True)
    name = Column(String(100))
    systolic = Column(Integer, nullable=False)
    diastolic = Column(Integer, nullable=False)
    pulse = Column(Integer, nullable=False)
    reading_time = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')

