#!/usr/bin/python3
""" unit test for Review class """
import os
import pep8
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str if os.getenv(
            "HBNB_TYPE_STORAGE") != "db" else None
        )

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")