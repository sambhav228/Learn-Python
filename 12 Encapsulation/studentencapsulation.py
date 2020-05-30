'''Implementing Encapsulation, so that we cannot access the private fields outside the class using name mangling too, i.e. by making getters and setters'''

class Student:
    def setId(self, id):    # Mutator or Setter Method
        self.id = id

    def getId(self):        # Accessor or Getter Method
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()

s.setId(201851024)
s.setName('Anubhav Madhav')

print(s.getId())
print(s.getName())