import pymongo


if __name__ == "__main__":
    print("welcome to Sangramdb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Sangram']
    collection = db['myFirstCollection']

    prev = {"name" : "Munmahesh"}
    nextt = {'$set':{"Address" : "mumbai"}}
    #collection.update_one(prev, nextt)
    db = collection.update_many(prev, nextt)
    print(db.modified_count)

    print("update done")