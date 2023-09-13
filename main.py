#!/usr/bin/env python3

import json


with open('user_details.json', 'r') as f:
    objs = json.loads(f.readline())
    for obj in objs:
        