from flask import Flask
import pandas as pd
import pyodbc
app= Flask(__name__)

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-C54N8MQU;'
        'DATABASE=master;'
        'UID=LAPTOP-C54N8MQU\laksh;'
        'Trusted_Connection=yes;'
    )
    return conn
# def get_db_connection():
    # conn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 17 for SQL Server};'
    #     'SERVER=LAPTOP-C54N8MQU;'
    #     'DATABASE=master;'
    #     'UID=LAPTOP-C54N8MQU\laksh;'
    #     'Trusted_Connection=yes;'  # Use Windows Authentication
    # )
    # return conn
@app.route('/')
def hello():
    a = "Hello, World"
    return(a)


@app.route('/data',methods=['GET'])
def get_data():
    conn = get_db_connection()
    query  = "Select * from Walmart"
    df = pd.read_sql(query ,conn).to_dict(orient='records')
    conn.close()
    return(df)

@app.route('/onlinefoods', methods=['GET'])
def put_data():
    conn = get_db_connection()
    query  = "Select * from onlinefoods1"
    df1 = pd.read_sql(query ,conn).to_dict(orient='records')
    conn.close()
    return(df1)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
    