#!/usr/bin/python3
""" unit test for Amenity class """
import os
import pep8
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ initialize test_Amenity """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name """
        new = self.value()
        self.assertEqual(type(new.name), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
