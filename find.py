import pymongo


if __name__ == "__main__":
    print("welcome to Sangramdb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['Sangram']
    collection = db['myFirstCollection']
    #one = collection.find_one({'name': 'Munmahesh'})
    # 1 for for show and 0 for hide
    many = collection.find({'name': 'Munmahesh'}, {'_id' : 0})
    for i in many:
        print(i)