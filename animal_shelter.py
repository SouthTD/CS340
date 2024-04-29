from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse


    

class AnimalShelter(object):
    records_updated = 0
    records_matched = 0
    records_deleted = 0

    def __init__(self, USER, PASS):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31105
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
       

    #create - adds a record in the dataset
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Request invalid, doc is empty")
    
    #read - reads information from a record in the dataset
    def read(self, criteria = None):
        if criteria is not None:
            _data = self.database.animals.find(criteria, {'_id' : 0})                   
        else:
            _data = self.database.animals.find({}, {'_id' : 0})                 
        return _data

    #update - updates information for a record in the dataset
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Request invalid, doc is empty")

    #delete - removes a record from the dataset
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document was found"
            return result
        else:
            raise Exception("Request invalid, doc is empty")