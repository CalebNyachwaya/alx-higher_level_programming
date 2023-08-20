#!/usr/bin/python3
""" class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Base class used to create database


class State(Base):
    """ Class States to create table in bd """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
