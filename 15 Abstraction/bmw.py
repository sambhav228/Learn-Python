''' Create an Abstract Class '''

from abc import abstractmethod, ABC
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):                            # Can be called by object of any of it's child class
        print("Car is Starting")

    def stop(self):                             # Can be called by object of any of it's child class
        print("Car is stopped")

    @abstractmethod                 # This method is imported from 'abc' module. And for that, BMW Class should also inherit 'ABC' Class in the same module
    def drive(self):                # This is an Abstract Method
        pass                        # Instead of 'pass', we can simply write any string too for e.g. Syntax: "svbhjasb'

class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)                 # Using super() inbuilt function to use constructor of parent class
        # or  # BMW.__init__(self, make, model, year)       # In case, if we do not want to use super(), we can use this i.e. using name of parent class
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):                            # Overriding - This method will override the start() method of parent class, i.e. this method will be executed
        super().start()                         # This will execute start() of parent class, i.e. it will print "Car is Starting"
        print("Button Start")                   # Same function name but different functionality

    def drive(self):
        print("Three Series is being driven")

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        # or # BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


    def drive(self):
        print("Five Series is being driven")

t = ThreeSeries(True, 'GTR', '15x', 2018)               # This is dynamic typing, so we get runtime polymorphism for free, since we need not mention the name of the class on left side as in Java
print(t.cruiseControlEnabled)
print(t.make)
print(t.model)
print(t.year)
t.start()                   # Inheriting the function of parent class
t.stop()                    # Inheriting the function of parent class
t.display()                 # Called it's own function

f = FiveSeries(False, 'GTX', '19y', 2019)
print(f.parkingAssistEnabled)
print(f.make)
print(f.model)
print(f.year)

# d = BMW('GTX', '19y', 2019)                     # This gives an TypeError: Can't instantiate abstract class BMW with abstract methods drive

'''Runtime Polymorphism'''

# Since the variable types ar dynamic we can get that runtime kind of polymorphism for free




'''Abstraction '''
# Abstract Method - A method in a Class, which do not have any body, used with '@abstractmethod' decorator in python. This decorator is imported from 'abc' module.
# Abstract Class - A class which has atleast one Abstract Method is known as an Abstract Class
# Interface - A class, which has only Abstract methods or we can say that a class in which all the methods are abstract methods is an Interface

# If a parent class has 2 abstract methods and 3 normal methods, then all it's child classes should also have 2 abstract methods and that too same in parameters. Though, it can have any number of normal methods or even none.
