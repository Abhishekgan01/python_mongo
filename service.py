from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = "mongodb+srv://abhishekganesh2002:1234@abhishek.bzqgvfv.mongodb.net/?retryWrites=true&w=majority&appName=abhishek"
client = MongoClient(mongo_uri)
db = client['dat']

collection = db['student']
def get_all_items():
    return list(collection.find({}, {'_id': 0}))

def add_item(item):
    result = collection.insert_one(item)
    return str(result.inserted_id)

def update_item(item_id, item):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item})
    return result.modified_count

def delete_item(item_id):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count