'''Define a Static Field (always defined globally in a class)'''

class Student:
    major = 'CSE'                       # Defining a static field (it is always defined globally)

    def __init__(self, rollno, name):
        self.name = name
        self.rollno = rollno

s1 = Student(1,'Anubhav Madhav')
s2 = Student(2,'Digant Goyal')

print(s1.name)
print(s1.rollno)
print(s1.major)             # Static field called using an Object

print(s2.name)
print(s2.rollno)
print(s2.major)             # Static field called using an Object


print(Student.major)        # Static field can also be called without creating an Object i.e. by using name of the 'class'