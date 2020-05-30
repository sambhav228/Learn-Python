"""Create an Inner Class and make it's Instance too"""

class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine Started")

c = Car("Lamborghini",2020)                     # Created an Instance/Object of the outer class
e = c.Engine(123)                               # Created an Instance/Object of the inner class using the Instance of the outer class
e.start()                                       # Called the function of the Inner class using the Instance of Inner class