import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.ganglion

print(db.collection_names())