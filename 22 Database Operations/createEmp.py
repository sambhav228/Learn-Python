'''Read all the rows from table in database at once'''

import mysql.connector

connection = mysql.connector.connect(host='localhost', database="myDB", user='root', password='your_ROOT_Password')

if connection.is_connected():
    print("Connected to mysql Database")

cursor = connection.cursor()

try:
    cursor.execute("insert into emp values (3,'John',10000)")
    connection.commit()             # Commit the changes
    print("Employee Added")
except:
    connection.rollback()           # This is for Transaction Management, we can rollback to initial stage

cursor.close()
connection.close()

'''Before executing this program please do enter some values in the 'emp' table usimg mysql workbench'''