#!/usr/bin/python3
"""defines a city class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class represtenting what city the rental property is located
    attributes-
    name (empty string)
    state_id (empty string but will become State.id
    """
    state_id = ""
    name = ""
