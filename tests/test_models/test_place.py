#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.place import Place


class test(unittest.TestCase):
    """
    tests if the attributes of User are correct datatype
    """
    def test_name_is_str(self):
        self.assertEqual(str, type(Place.name))
    def test_city_id_is_str(self):
        self.assertEqual(str, type(Place.city_id))
    def test_user_id_is_str(self):
        self.assertEqual(str, type(Place.user_id))
    def test_description_is_str(self):
        self.assertEqual(str, type(Place.description))
    def test_number_rooms_is_int(self):
        self.assertEqual(int, type(Place.number_rooms))
    def test_number_bathrooms_is_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))
    def test_max_guest_is_int(self):
        self.assertEqual(int, type(Place.max_guest))
    def test_price_by_night_is_int(self):
        self.assertEqual(int, type(Place.price_by_night))
    def test_latitude_is_float(self):
        self.assertEqual(float, type(Place.latitude))
    def test_longitude_is_float(self):
        self.assertEqual(float, type(Place.longitude))
    def test_amenity_id_is_list(self):
        self.assertEqual(list, type(Place.amenity_id))


if __name__ == "__main__":
    unittest.main()
