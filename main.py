#!/usr/bin/env python3
"""Populating the database"""

from app import db
from app.models import *
import json
import requests
import random
from werkzeug.security import generate_password_hash, check_password_hash
import asyncio
from datetime import datetime


address = Address.query.filter_by(cus_id=4).first()
db.session.delete(address)
address = Address.query.filter_by(cus_id=4).first()
print(Address)
    
    