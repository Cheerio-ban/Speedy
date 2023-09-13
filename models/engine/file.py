#!/usr/bin/env/python3
"""File storage"""


import json
import os

class FileStorage:

    def all(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        with open( os.path.join(basedir, 'user_details.json')) as f:
            obj = json.loads(f.readline())
        return obj