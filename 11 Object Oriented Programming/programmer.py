'''Print the details of a Programmer using SETTER and GETTER'''

class Programmer:
    def setName(self, n):               # Setter method, it always takes a parameter which we assign them into object variables
        self.name = n

    def getName(self):                  # Getter method, to access the value of Setter method
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, tech):
        self.technologies = tech

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName('Anubhav Madhav')
p1.setSalary(10000000000000000000000000)                        # It's my Income per month, not salary
p1.setTechnologies('Artificial Intelligence Engineer')


print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
