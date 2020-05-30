print()                                      # Output: 

print('Hello')                               # Output: Hello

print('Hello'*3)                             # Output: HelloHelloHello

print('All the Power is with you')           # Output: All the Power is with you

print('All the Power \nis with you')         # Output: All the Power 
                                                #      is with you
a,b = 10,20
print(a,b)                                   # Output: 10 20


print(a,b,sep=',')                           # Output: 10,20

print(a,b,sep='++++')     # used separator   # Output: 10++++20





'''Print and String Formatting'''

name = 'Anubhav'
marks = 90.4678

print("Name is",name, "Marks are",marks)                        # Output: Name is Anubhav Marks are 90.4678

print("Name is %s, Marks are %f"%(name,marks))                  # Output: Name is Anubhav, Marks are 90.467800   

print("Name is %s, Marks are %.2f"%(name,marks))                # Output: Name is Anubhav, Marks are 90.47

print("Name is {}, Marks are {}".format(name,marks))            # Output: Name is Anubhav, Marks are 90.4678

print("Name is {0}, Marks are {1}".format(name,marks))          # Output: Name is Anubhav, Marks are 90.4678

