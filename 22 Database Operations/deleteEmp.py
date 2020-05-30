'''Read all the rows from table in database at once'''

import mysql.connector


def delete(id):
    connection = mysql.connector.connect(host='localhost', database="myDB", user='root', password='your_ROOT_Password')

    if connection.is_connected():
        print("Connected to mysql Database")
        cursor = connection.cursor()
        str = "delete from emp where id='%d'"
        args = (id)
    try:
        cursor.execute(str %args)
        connection.commit()             # Commit the changes
        print("Employee Deleted")
    except:
        connection.rollback()           # This is for Transaction Management, we can rollback to initial stage
    finally:
        cursor.close()
        connection.close()

empID = int(input("Enter EMP ID to be deleted:"))
delete(empID)

'''Before executing this program please do enter some values in the 'emp' table usimg mysql workbench'''


'''
Similarly, we can do it for 'UPDATE' by creating a function 'Update'
'''