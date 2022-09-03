import pymongo


if __name__ == "__main__":
    print("welcome to Sangramdb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    alldbs = client.list_database_names()
    print(alldbs)