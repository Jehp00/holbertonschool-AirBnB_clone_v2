#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
import os
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """getter for list of cities"""
            List_cities = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    List_cities.append(city)
            return List_cities
