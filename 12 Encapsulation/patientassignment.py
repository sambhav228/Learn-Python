class Patient:
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSSN(self, ssn):
        self.ssn = ssn

    def getSSN(self):
        return self.ssn

p = Patient()

p.setId(1)
p.setName('Chinese')
p.setSSN(255)

print(p.getId())
print(p.getName())
print(p.getSSN())