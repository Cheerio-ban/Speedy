#!/usr/bin/env/python3
"""DB storage"""


import json
import os
from app import db
from models import *
from datetime import datetime

class DBStorage:
    """This alters and modifies the database"""

    DATETIME_FORMAT = '%m/%d/%Y'
    def all(self, cls):
        """Generate all data on a particular class from the db"""
        objs = cls.query.all()
        return objs
    
    def to_json(self, obj):
        dict_obj = obj.__dict__
        for k, v in dict_obj.items():
            if type(v) == datetime:
                dict_obj[k] = datetime.strftime(DBStorage.DATETIME_FORMAT, v)
        del dict_obj['_sa_instance_state']
        del dict_obj['password_hash']
        return dict_obj

    def reload(self):
        """reload the database"""
        pass