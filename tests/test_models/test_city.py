#!/usr/bin/python3
""" unit test for Place class """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )
    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
