#!/usr/bin/python3
""" unit test for User class """
import os
import pep8
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
