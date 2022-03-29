import requests, json
from config import *

BASE_URL = 'a'
ACCOUNT_URL = 'a'
ORDERS_URL = 'a'
HEADERS = {}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)
