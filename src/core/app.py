import json
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


def init_db():
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '../../config/database.json',
    )
    database_config = json.loads(open(config_file).read())

    client = MongoClient(database_config['host'], database_config['port'])
    return client[database_config['name']]
