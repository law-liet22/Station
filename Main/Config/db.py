import mysql.connector
from dotenv import dotenv_values

dotValues = dotenv_values(".env")
myHost = dotValues["DB_HOST"]
myUser = dotValues["DB_USER"]
myPassword = dotValues["DB_PASSWORD"]
myDbName = dotValues["DB_NAME"]

def connectToBDb(_host: str=myHost, _user: str=myUser, _password: str=myPassword, _port: str=3306, _database: str=myDbName):
    myDb = mysql.connector.connect(
        host = _host,
        user = _user,
        password = _password,
        port = _port,
        database = _database
    )

    return myDb

try:
    myDb = connectToBDb()
    

    myCursor = myDb.cursor()

    myCursor.execute("SHOW DATABASES")

    for i in myCursor:
        if i[0] == myDbName or "information_schema":
            print(i[0])

        else:
            myCursor.execute("CREATE TABLE maTable")

    myCursor.execute("SHOW TABLES")

    for i in myCursor:
        print(i[0])

    myCursor.close()

except ConnectionError as ce:
    print(ce)
