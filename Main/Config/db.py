import mysql.connector
from dotenv import *

dotValues = dotenv_values(".env")
myHost = dotValues["DB_HOST"]
myUser = dotValues["DB_USER"]
myPassword = dotValues["DB_PASSWORD"]


try:
    mydb = mysql.connector.connect(
        host = myHost,
        user = myUser,
        password = myPassword,
        port = 3306
    )
except ConnectionError as ce:
    print(ce)
