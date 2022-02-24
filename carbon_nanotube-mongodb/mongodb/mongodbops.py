import pymongo
import csv
class MongoDbOperation:
    def __init__(self, username, password):
        try:
            self.username=username
            self.password=password
            self.url =f"mongodb+srv://{self.username}:{self.password}@cluster0.n75mm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

        except Exception as e:
            raise Exception(f"something went wrong to initialize the process:{str(e)}")

    def getMongoClient(self):
        '''It returns MongoClient'''
        try:
            client=pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            raise Exception(f"something went wrong to create MongoClient: {str(e)}")

    def getDatabase(self, dbName):
        '''It returns database'''
        try:
            client=self.getMongoClient()
            database=client[dbName]
            # client.close()
            return database
        except Exception as e:
            raise Exception(f"something went wrong to get Database: {str(e)}")

    def getCollection(self,dbName,collectionName):
        '''It returns collection'''
        try:
            database=self.getDatabase(dbName)
            collection=database[collectionName]
            return collection
        except Exception as e:
            raise Exception(f"something went wrong to get collection: {str(e)}")
    def isDatabasePresent(self,dbName):
        '''It returns True if database present'''
        try:
            client=self.getMongoClient()
            if dbName in client.list_database_names():
                return True
            else:
                return False
        except Exception as e:
            raise Exception(f"something went wrong to check presence of Database:{dbName}: {str(e)}")

    def isCollectionPresent(self, dbName, collectionName):
        '''It returns True if collection present'''
        try:
            if self.isDatabasePresent(dbName):
                database = self.getDatabase(dbName)
                if collectionName in database.list_collection_names():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            raise Exception(f"something went wrong to check presence of Collection:{collectionName}: {str(e)}")

    def createDatabase(self, dbName):
        '''It creates database'''
        try:
            if self.isDatabasePresent(dbName):
                return f"DB:{dbName} already exsists"
            else:
                client = self.getMongoClient()
                database=client[dbName]
            return f"DB:{dbName} created successfully"
        except Exception as e:
            raise Exception(f"something went wrong to create Database:{dbName}: {str(e)}")
    def createCollection(self, dbName,collectionName):
        '''It creates collection'''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                return f"Collection:{collectionName} already exsists in DB:{dbName}"
            else:
                database = self.getDatabase(dbName)
                collection = database[collectionName]
                return f"Collection:{collectionName} in DB:{dbName} created successfully"

        except Exception as e:
            raise Exception(f"something went wrong to create Collection:{collectionName}: {str(e)}")

    def insertOneData(self,dbName, collectionName, data):
        ''' It insertes one data into collection'''
        try:
            collection=self.getCollection(dbName,collectionName)
            collection.insert_one(data)
            return f"Data inserted into Collection:{collectionName} of Database:{dbName}"
        except Exception as e:
            raise Exception(f"something went wrong to insert one data: {str(e)}")

    def insertManyData(self,dbName, collectionName, data):
        '''It inserts many data into collection'''
        try:
            collection=self.getCollection(dbName,collectionName)
            collection.insert_many(data)
            return f"Data inserted into Collection:{collectionName} of Database:{dbName}"

        except Exception as e:
            raise Exception(f"something went wrong to insert many data: {str(e)}")

    def uploadDataset(self, dataset, dbName, collectionName):
        '''It uploads dataset into collection'''
        try:
            with open(dataset, 'r') as f:
                col = f.readline().rstrip().split(';')
                next(f)
                csv_reader = csv.reader(f, delimiter=';')
                l = []
                for data in csv_reader:
                    d = {col[i]: data[i] for i in range(len(col))}
                    l.append(d)
            collection=self.getCollection(dbName,collectionName)
            collection.insert_many(l)
            return f"Dataset:{dataset} uploaded successfully in Collection:{collectionName} of Database:{dbName}"

        except Exception as e:
            raise Exception(f"something went wrong to upload dataset:{dataset}: {str(e)}")

    def getData(self,dbName,collectionName,limit=5):
        '''It gives data one by one'''
        try:
            if self.isCollectionPresent(dbName, collectionName):
                collection=self.getCollection(dbName,collectionName)
                data= collection.find().limit(limit)
                return data
        except Exception as e:
            raise Exception(f"something went wrong to find data: {str(e)}")

    def filter(self,dbName,collectionName, condition, limit=5):
        '''It gives data one by one based on given condition'''
        try:
            if self.isCollectionPresent(dbName, collectionName):
                collection=self.getCollection(dbName,collectionName)
                data=collection.find(condition).limit(limit)
                return data

        except Exception as e:
            raise Exception(f"something went wrong to filter data: {str(e)}")

    def updateOne(self,dbName, collectionName, present_data, new_data):
        '''It updates one data '''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                collection=self.getCollection(dbName,collectionName)
                new_data={'$set':new_data}
                collection.update_one(present_data,new_data)
                return "Dataset updated successfully"

        except Exception as e:
            raise Exception(f"something went wrong to update one data: {str(e)}")

    def updateAll(self,dbName, collectionName, present_data, new_data):
        '''It updates all data'''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                collection=self.getCollection(dbName,collectionName)
                new_data={'$set':new_data}
                collection.update_many(present_data,new_data)
                return "Dataset updated successfully"
        except Exception as e:
            raise Exception(f"something went wrong to update All data: {str(e)}")

    def deleteOneRecord(self,dbName,collectionName,condition):
        '''It deletes one record based on condition'''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                collection=self.getCollection(dbName,collectionName)
                collection.delete_one(condition)
                return f"One record based on condition:{condition} deleted"
        except Exception as e:
            raise Exception(f"something went wrong to delete one record: {str(e)}")

    def deleteAllRecord(self,dbName,collectionName,condition):
        '''It deletes all data based on condition'''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                collection=self.getCollection(dbName,collectionName)
                collection.delete_many(condition)
                return f"All record based on condition:{condition} deleted"
        except Exception as e:
            raise Exception(f"something went wrong to delete All record: {str(e)}")


    def dropCollection(self, dbName, collectionName):
        '''It drops collection'''
        try:
            if self.isCollectionPresent(dbName,collectionName):
                collection=self.getCollection(dbName,collectionName)
                collection.drop()
                return f"Collection:{collectionName} of Database:{dbName} dropped successfully"

        except Exception as e:
            raise Exception(f"something went wrong to drop collection: {str(e)}")

   
