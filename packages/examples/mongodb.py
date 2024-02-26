#--param MONGODB_URL $MONGODB_URL

from pymongo import MongoClient
from bson import json_util

def main(args):
    client = MongoClient(args.get("MONGODB_URL"))
    db = client.get_database()
    data = db["data"]
    mydict = { "hello": "world" }
    data.insert_one(mydict)
    res = data.find_one()
    return {"body": json_util.dumps(res)}