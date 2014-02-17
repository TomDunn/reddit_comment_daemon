from os import environ

from pymongo import MongoClient

client = MongoClient(environ['mongo_uri'])
db     = client['reddit-test']
