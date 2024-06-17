import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass123"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE EMP_MM")
mycursor.execute("CREATE DATABASE EMP_MM")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)