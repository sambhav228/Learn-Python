class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):                            # Can be called by object of any of it's child class
        print("Car is Starting")

    def stop(self):                             # Can be called by object of any of it's child class
        print("Car is stopped")


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


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        # or # BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


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



'''Runtime Polymorphism'''

# Since the variable types ar dynamic we can get that runtime kind of polymorphism for free