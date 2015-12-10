import pymongo
from bson.son import SON
from pymongo import MongoClient

# encoding=utf-8
__author__ = 'Hinsteny'

print(pymongo.get_version_string())


class SingleClient(object):
    '''
    Single Client hold the client object
    '''

    client = MongoClient('127.0.0.1', 27017)
    client.the_database.authenticate('hinsteny', 'welcome', source='admin', mechanism='SCRAM-SHA-1')

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(SingleClient, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

def getClient():
    client = MongoClient('127.0.0.1', 27017)
    client.the_database.authenticate('hinsteny', 'welcome', source='admin', mechanism='SCRAM-SHA-1')
    return client

def test_connection():
    client = getClient()
    db = client.cube_test
    query = {}
    cursor = db.user.find(query)
    print(cursor.count())
    print(cursor[0])

def test_addUser():
    client = getClient()
    db = client.admin
    query = {}
    cursor = db.system.users.find(query)
    if cursor.count() == 0 :
        db.runCommand({createUser})({"user":"admin","pwd":"welcome","roles":["root"]})
    else:
        print(cursor[0])

def create_test_data(db):
    db.things.drop()
    result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},{"x": 2, "tags": ["cat"]},{"x": 2, "tags": ["mouse", "cat", "dog"]},{"x": 3, "tags": ["eat","pear"]}])
    print(result.inserted_ids)

def doAggregation(collection, pipeline):
    print(list(collection.aggregate(pipeline)))

# Do test
if __name__ == "__main__":
    test_connection()
    # test_addUser()
    db = getClient().aggregation_example
    create_test_data(db)
    pipeline = [
         {"$unwind": "$tags"},
         {"$group": {"_id": "", "count": {"$sum": "$x"}}},
         {"$sort": SON([("count", -1), ("_id", -1)])}
     ]
    doAggregation(db.things, pipeline)