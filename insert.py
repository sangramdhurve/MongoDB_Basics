import pymongo


if __name__ == "__main__":
    print("welcome to Sangramdb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Sangram']
    collection = db['myFirstCollection']
    dictionary = [{"name":"Sangram", "marks":90, "Subject":"Physics"}, {"_id": 8, "name":"Cahand", "marks":80, "Subject":"Physics"}, {"name":"Munmahesh", "marks":60, "Subject":"Physics"}]
    collection.insert_many(dictionary)
    print("data inserted")