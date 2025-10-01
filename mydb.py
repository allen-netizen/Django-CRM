import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderCo")

print("All Done!")