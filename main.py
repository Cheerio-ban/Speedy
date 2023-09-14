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


pins = {}
accounts = Account.query.all()
for account in accounts:
    print(account.account_pin)

    
    