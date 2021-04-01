import mysql.connector

def connect(db):
    try:
        mydb = mysql.connector.conect(
            host = 'localhost',
            user = 'admin',
            passwd = 'B3b3d0ur0',
            database = db
        )
    except Exception:
        return Exception
    return mydb