from flask import Flask, request, jsonify
app = Flask(__name__)
import logging as lg
lg.basicConfig(filename='apilog.log', level=lg.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
#*******************************************************MONGODB*************************************************************************
@app.route('/mongo_createCollection', methods=['GET', 'POST'])
def createCollection():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']

        import pymongo
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database=client[database]
        collection = database[collection]
        lg.info("mongodb: collection created")
        return jsonify("mongodb: collection created")

    except Exception as e:
        lg.error("mongodb: error occured during collectin creation: ", e)
        return jsonify("mongodb: error occured during collectin creation")


@app.route('/mongo_insertIntoTable', methods=['POST', 'GET'])
def insertIntoTable():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']
        record = request.json['record']

        import pymongo
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client[database]
        collection = database[collection]
        collection.insert_one(record)
        lg.info("mongodb:Inserted into table")
        return jsonify("mongodb:Inserted into table!")
    except Exception as e:
        lg.error("mongodb:error occured durning insert into table: ", e)
        return jsonify("mongodb:error occured durning insert into table")


@app.route('/mongo_updateTable', methods=['POST', 'GET'])
def updateTable():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']
        old_data = request.json['old_data']
        new_data = request.json['new_data']
        import pymongo
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client[database]
        collection = database[collection]
        old_data = old_data
        new_data = {'$set': new_data}
        collection.update_many(old_data, new_data)
        lg.info("mongodb:Table updated!")
        return jsonify("mongodb:Table updated!")
    except Exception as e:
        lg.error("mongodb:error occured during updation of table: ", e)
        return jsonify("mongodb:error occured during updation of table")


@app.route('/mongo_bulkUpload', methods=['POST', 'GET'])
def bulkUpload():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']
        filepath = request.json['filepath']

        import pymongo
        import pandas as pd
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client[database]
        collection = database[collection]
        df = pd.read_csv(filepath)
        for i, row in df.iterrows():
            collection.insert_one(dict(row))
        lg.info("mongodb:Bulk data uploaded!")
        return jsonify("mongodb:Bulk data uploaded!")
    except Exception as e:
        lg.error("mongodb:error occured during bulk data upload: ", e)
        return jsonify("mongodb:error occured during bulk data upload")


@app.route('/mongo_deleteFromTable', methods=['POST', 'GET'])
def deleteFromTable():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']
        condition  = request.json['condition']
        import pymongo
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client[database]
        collection = database[collection]
        collection.delete_many(condition)
        lg.info("mongodb:Row(s) deleted from table!")
        return jsonify("mongodb:Row(s) deleted from table!")
    except Exception as e:
        lg.error("mongodb:error occured during delete of row(s): ", e)
        return jsonify("mongodb:error occured during delete of row(s)")

@app.route('/mongo_downloadTable', methods=['POST', 'GET'])
def downloadTable():
    try:
        password = request.json['password']
        database = request.json['database']
        collection = request.json['collection']
        downloadPath = request.json['downloadPath']

        import pymongo
        import pandas as pd
        client = pymongo.MongoClient(f"mongodb+srv://test:{password}@cluster0.jfhhu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = client[database]
        collection = database[collection]
        df = pd.DataFrame(collection.find())
        df.to_csv(downloadPath)
        lg.info("mongodb:Data downloaded!")
        return jsonify("mongodb:Data downloaded!")
    except Exception as e:
        lg.error("mongodb:error occured during download of data: ", e)
        return jsonify("mongodb:error occured during download of data")










if __name__ == '__main__':
    app.run()