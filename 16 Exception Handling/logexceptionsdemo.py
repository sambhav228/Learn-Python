import logging

logging.basicConfig(filename="mylog2.log", level = logging.DEBUG)



try:
    f = open("myfile", "w")
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    logging.info("Division in Progress")
    c = a/b
    f.write("Writing %d into file" %c)

except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by Zero")

else:
    print("You have entered a non zero number")

finally:
    f.close()  # Writing f.close() in finally block because whether the error appears or not, we always want to close the file, so we will use f.close() in finally.
    print("File Closed")

print("Code after that exception")