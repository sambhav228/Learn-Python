import mysql.connector

connection = mysql.connector.connect(host='localhost', database="myDB", user='root', password='your_ROOT_Password')

if connection.is_connected():
    print("Connected to mysql Database")

cursor = connection.cursor()

cursor.execute("select * from emp")

row = cursor.fetchone()         # fetches one row at a time

while row is not None:          # This will fetch each row one by one until the row is 'None' i.e. until there is no row
    print(row)
    row = cursor.fetchone()

cursor.close()
connection.close()

'''Before executing this program please do enter some values in the 'emp' table usimg mysql workbench'''