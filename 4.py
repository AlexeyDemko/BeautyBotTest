from pymongo import MongoClient, ASCENDING
from pymongo.operations import IndexModel
from datetime import datetime, timedelta


DOCUMENT_ID = "document_id"

client = MongoClient('mongodb+srv://username:password@cluster.mongodb.net/db')

db = client['database']
collection = db['collection']


def create_ttl_index():
    index_model = IndexModel([("expiry_time", ASCENDING)], expireAfterSeconds=0)
    collection.create_indexes([index_model])


def set_expiry_time():
    return datetime.utcnow() + timedelta(hours=24)


def insert_document():
    # If we want to delete documents after 24h
    document = {"field1": "value1", "expiry_time": set_expiry_time()}
    collection.insert_one(document)


def update_document_expiry_date():
    # To set an expiry date for an existing document
    collection.update_one({"_id": DOCUMENT_ID}, {"$set": {"expiry_time": set_expiry_time()}})


def main():
    create_ttl_index()
    insert_document()
    update_document_expiry_date()


if __name__ == "__main__":
    main()
