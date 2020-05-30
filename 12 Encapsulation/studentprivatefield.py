"""Mark a field as Private and Name Mangling, using which we can access the private field through the object"""

'''Using Public Field'''
class Student:
    def __init__(self):
        self.id = 123                   # These 2 fields 'id' and 'name' are public (not private). To, make those fields private we will place 2 underscore '__' before their name
        self.name = 'Anubhav'

s = Student()
print(s.id)
print(s.name)


'''Using Private Field'''
class Student2:
    def __init__(self):
        self.__id = 12                  # This is a private field, as we have placed 2 underscores ('__') just before the name of the fields
        self.__name = 'Kittu'

# s2 = Student2()                         # This do not calls the fields because it is outside the class and the fields are private
# print(s2.id)                            # This gives an error
# print(s2.name)                          # This gives an error




'''Using Private field with NAME WANGLING'''

class Student3:
    def __init__(self):
        self.__id = 1
        self.__name = 'Madhav'

s3 = Student3()
print(s3._Student3__id)                     # This is called NAME MANGLING. Syntax: "object._classname__privatefield"
print(s3._Student3__name)