#!/usr/bin/python3
""" unit test for Place class """
import os
import pep8
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if os.getenv(
                "HBNB_TYPE_STORAGE") != "db" else None
            )

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
