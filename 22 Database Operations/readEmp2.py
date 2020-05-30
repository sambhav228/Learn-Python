'''Read all the rows from table in database at once'''

import mysql.connector

connection = mysql.connector.connect(host='localhost', database="myDB", user='root', password='your_ROOT_Password')

if connection.is_connected():
    print("Connected to mysql Database")

cursor = connection.cursor()

cursor.execute("select * from emp")

rows = cursor.fetchall()         # fetches all the rows at once
print("Total No.Of Rows:",cursor.rowcount)


for row in rows:          # This will fetch all rows at once
    print(row)
    row = cursor.fetchone()

cursor.close()
connection.close()

'''Before executing this program please do enter some values in the 'emp' table usimg mysql workbench'''