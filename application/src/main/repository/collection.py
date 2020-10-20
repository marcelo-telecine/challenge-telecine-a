from main.common.database import DBClient
from main.model.collection import Collection as CollectionModel

class Collection():

    collection = "currencies"

    @staticmethod
    def get_collection():
        mongodb = DBClient.conn()
        return mongodb[Collection.collection]


    @staticmethod
    def find(query):
        mongo_currencies_collection = Collection.get_collection()
        documents = mongo_currencies_collection.find(query)
        output = []

        if documents:
            for doc in documents:
                output.append(CollectionModel().load(doc))

        return output


    @staticmethod
    def create(data):
        mongo_currencies_collection = Collection.get_collection()

        insert_result = mongo_currencies_collection.insert_one(data)

        if not insert_result.acknowledged:
            raise Exception('Error on creating collection')

        data['_id'] = insert_result.inserted_id

        object = CollectionModel().load(data)

        return object
