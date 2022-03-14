from flask import Flask, request, jsonify
app = Flask(__name__)
import logging as lg
lg.basicConfig(filename='apilog.log', level=lg.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
#********************************************************CASSANDRA******************************************************************
def cassndra_connct(client_id, client_secret):
    from cassandra.cluster import Cluster
    from cassandra.auth import PlainTextAuthProvider

    cloud_config = {
        'secure_connect_bundle': 'E:\secure-connect-test.zip'
    }
    auth_provider = PlainTextAuthProvider(client_id, client_secret)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    return session

@app.route('/cassandra_createTable', methods=['GET', 'POST'])
def createTable():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            col1=request.json['col1']
            col2=request.json['col2']
            col3=request.json['col3']
            col4=request.json['col4']

            query=f"CREATE TABLE {keyspace}.{table_name}({col1}, {col2}, {col3}, {col4});"
            session=cassndra_connct(client_id, client_secret)
            session.execute(query)
            lg.info("cassandra:Table created!")
            return jsonify("cassandra:Table created!")
        except Exception as e:
            lg.error("cassandra:error occured during table creation: ", e)
            return "cassandra:error occured during table creation"


@app.route('/cassandra_insertIntoTable', methods=['GET', 'POST'])
def insertIntoTable():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            col1=request.json['col1']
            col2=request.json['col2']
            col3=request.json['col3']
            col4=request.json['col4']

            query=f"INSERT INTO {keyspace}.{table_name}({col1[0]}, {col2[0]}, {col3[0]}, {col4[0]}) VALUES({col1[1]}, '{col2[1]}', {col3[1]}, '{col4[1]}');"
            session=cassndra_connct(client_id, client_secret)
            session.execute(query)
            lg.info("cassandra:Inserted into table")
            return jsonify("cassandra:Inserted into table")
        except Exception as e:
            lg.error("cassandra:error occured durning insert into table: ", e)
            return "cassandra:error occured durning insert into table"

@app.route('/cassandra_updateTable', methods=['GET', 'POST'])
def updateTable():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            columnToUpdate=request.json['columnToUpdate']
            updatedValue=request.json['updatedValue']
            id=request.json['id']

            if type(updatedValue)==str:
                query=f"UPDATE {keyspace}.{table_name} SET {columnToUpdate} = '{updatedValue}' WHERE id={id};"
            else:
                query=f"UPDATE {keyspace}.{table_name} SET {columnToUpdate} = {updatedValue} WHERE id={id};"

            session=cassndra_connct(client_id, client_secret)
            session.execute(query)
            lg.info("cassandra:Table updated!")
            return jsonify("cassandra:Table updated!")
        except Exception as e:
            lg.error("cassandra:error occured during updation of table: ", e)
            return "cassandra:error occured during updation of table"

@app.route('/cassandra_bulkUpload', methods=['GET', 'POST'])
def bulkUpload():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            filepath=request.json['filepath']

            import pandas as pd
            df = pd.read_csv(filepath)
            col=df.columns
            for i, row in df.iterrows():
                row=list(row)
                query=f"INSERT INTO {keyspace}.{table_name}({col[0]}, {col[1]}, {col[2]}, {col[3]}) VALUES({row[0]}, '{row[1]}', {row[2]}, '{row[3]}');"
                session=cassndra_connct(client_id, client_secret)
                session.execute(query)
            lg.info("cassandra:Bulk data uploaded!")
            return jsonify("cassandra:Bulk data uploaded!")
        except Exception as e:
            lg.error("cassandra:error occured during bulk data upload: ", e)
            return "cassandra:error occured during bulk data upload"


@app.route('/cassandra_deleteFromTable', methods=['GET', 'POST'])
def deleteFromTable():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            id=request.json['id']

            query=f"DELETE FROM {keyspace}.{table_name} WHERE id={id};"
            session=cassndra_connct(client_id, client_secret)
            session.execute(query)
            lg.info("Row(s) deleted from table!")
            return jsonify("Row(s) deleted from table!")
        except Exception as e:
            lg.error("cassandra:error occured during delete of row(s): ", e)
            return "cassandra:error occured during delete of row(s)"


@app.route('/cassandra_downloadTable', methods=['GET', 'POST'])
def downloadTable():
        try:
            keyspace=request.json['keyspace']
            client_id=request.json['client_id']
            client_secret=request.json['client_secret']
            table_name=request.json['table_name']
            downloadpath=request.json['downloadpath']


            import pandas as pd
            query=f"SELECT * FROM {keyspace}.{table_name};"
            session=cassndra_connct(client_id, client_secret)
            df=session.execute(query)
            df=pd.DataFrame(df)
            df.to_csv(downloadpath)
            lg.info("cassandra:Data downloaded!")
            return jsonify("cassandra:Data downloaded!")
        except Exception as e:
            lg.error("cassandra:error occured during download of data: ", e)
            return "cassandra:error occured during download of data"


if __name__ == '__main__':
    app.run()