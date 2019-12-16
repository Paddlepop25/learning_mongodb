import pymongo
import os

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = 'myTestDB'
COLLECTION_NAME = 'myFirstMDB'

def mongo_connect(url):
    try:
        connection = pymongo.MongoClient(url)
        print('Mongo is conneted! WOOHOO')
        return connection
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e
        
connection = mongo_connect(MONGODB_URI)

collection = connection[DBS_NAME][COLLECTION_NAME]

documents = collection.find()

for doc in documents:
    print(doc)
        