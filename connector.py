import mysql.connector

mydb = mysql.connector.connect( host="localhost",user="root",passwd="mp10d9090")
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
