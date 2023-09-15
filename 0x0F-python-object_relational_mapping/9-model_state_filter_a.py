#!/usr/bin/python3
#Author: MikiasHailu
""" This modul is the state module."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class State(Base):
    """ This represents the base class """
    __tablename__ = "states"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = Column(
            String(length=128),
            nullable=False
            )
