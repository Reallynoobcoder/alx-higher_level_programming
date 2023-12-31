#!/usr/bin/python3
"""import SQLalchemy"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class City(Base):
    """Class city"""

    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False
                      )
