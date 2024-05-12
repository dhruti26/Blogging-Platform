from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.Blogging
blogs_collection=db["blogs"]


try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)    