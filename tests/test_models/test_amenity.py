#!/usr/bin/python3
"""module test amenity"""
from test.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """class testing amenity"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"

    def test_name2(self):
        """ """
        new = self.name
        self.assertEqual(type(new), str)
