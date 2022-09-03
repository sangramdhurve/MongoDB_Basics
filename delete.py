import pymongo


if __name__ == "__main__":
    print("welcome to Sangramdb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['Sangram']
    collection = db['myFirstCollection']

    prev = {"name" : "Munmahesh"}
    db = collection.delete_one(prev)
    #db = collection.delete_many(prev, nextt)
    print(db.deleted_count)

    print("delete done")