from flask import Flask, request, jsonify
app = Flask(__name__)
import logging as lg
lg.basicConfig(filename='apilog.log', level=lg.INFO, format="%(asctime)s  %(levelname)s  %(message)s")

#*********************************************************SQL*****************************************************************************
@app.route('/sql_createTable', methods=['POST'])
def createTable():
        try:
            host=request.json['host']
            database=request.json['database']
            user=request.json['user']
            password=request.json['password']
            table_name=request.json['table_name']
            col1=request.json['col1']
            col2=request.json['col2']
            col3=request.json['col3']
            col4=request.json['col4']

            import mysql.connector as connection
            mydb=connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
            query=f"CREATE TABLE {table_name}({col1},{col2},{col3},{col4});"
            cursor=mydb.cursor()
            cursor.execute(query)
            lg.info("Table created!")
            return jsonify("Table created!")
        except Exception as e:
            lg.error("error occured during table creation: ", e)
            return "error occured during table creation"


@app.route('/sql_insertIntoTable', methods=['POST', 'GET'])
def insertIntoTable():
    try:
        host = request.json['host']
        database = request.json['database']
        user = request.json['user']
        password = request.json['password']
        table_name = request.json['table_name']
        col1 = request.json['col1']
        col2 = request.json['col2']
        col3 = request.json['col3']
        col4=request.json['col4']

        import mysql.connector as connection
        mydb = connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
        query = f"INSERT INTO {table_name} VALUES({col1},'{col2}',{col3},'{col4}');"
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.commit()
        lg.info("Inserted into table")
        return jsonify("Inserted into table!")
    except Exception as e:
        lg.error("error occured durning insert into table: ", e)
        return "error occured durning insert into table"

@app.route('/sql_updateTable', methods=['POST','GET'])
def updateTable():
    try:
        host = request.json['host']
        database = request.json['database']
        user = request.json['user']
        password = request.json['password']
        table_name = request.json['table_name']
        colToUpdate = request.json['colToUpdate']
        updatedValue = request.json['updatedValue']
        condition = request.json['condition']

        import mysql.connector as connection
        mydb = connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
        if type(updatedValue)==str:
            query = f"UPDATE {table_name} SET {colToUpdate}='{updatedValue}' {condition};"
        else:
            query = f"UPDATE {table_name} SET {colToUpdate}={updatedValue} {condition};"
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.commit()
        lg.info('Table updated!')
        return jsonify("Table updated!")

    except Exception as e:
        lg.error("error occured during updation of table: ", e)
        return "error occured during updation of table"


@app.route('/sql_bulkUpload', methods=['POST','GET'])
def bulkUpload():
    try:
        host = request.json['host']
        database = request.json['database']
        user = request.json['user']
        password = request.json['password']
        table_name = request.json['table_name']
        filepath = request.json['filepath']
        import mysql.connector as connection
        import pandas as pd
        mydb = connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
        df=pd.read_csv(filepath)
        for i,row in df.iterrows():
            query=f"INSERT INTO {table_name} VALUES(%s, %s, %s, %s);"
            cursor = mydb.cursor()
            cursor.execute(query, tuple(row))
            mydb.commit()
        lg.info("Bulk data uploaded!")
        return jsonify("Bulk data uploaded!")

    except Exception as e:
        lg.error("error occured during bulk data upload: ", e)
        return "error occured during bulk data upload"

@app.route('/sql_deleteFromTable', methods=['POST','GET'])
def deleteFromTable():
    try:
        host = request.json['host']
        database = request.json['database']
        user = request.json['user']
        password = request.json['password']
        table_name = request.json['table_name']
        condition = request.json['condition']

        import mysql.connector as connection
        mydb = connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
        query = f"DELETE FROM {table_name} {condition};"
        cursor = mydb.cursor()
        cursor.execute(query)
        mydb.commit()
        lg.info("Row(s) deleted from table!")
        return jsonify("Row(s) deleted from table!")

    except Exception as e:
        lg.error('error occured during delete of row(s): ', e)
        return "error occured during delete of row(s)"

@app.route('/sql_downloadTable', methods=['POST','GET'])
def downloadTable():
    try:
        host = request.json['host']
        database = request.json['database']
        user = request.json['user']
        password = request.json['password']
        table_name = request.json['table_name']
        downloadPath = request.json['downloadPath']

        import pandas as pd
        import mysql.connector as connection
        mydb = connection.connect(host=host, database=database, user=user, password=password, use_pure=True)
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, mydb)
        df.to_csv(downloadPath)
        lg.info("Data downloaded!")
        return jsonify("Data downloaded!")

    except Exception as e:
        lg.error("error occured during download of data: ", e)
        return "error occured during download of data"


if __name__ == '__main__':
    app.run()
