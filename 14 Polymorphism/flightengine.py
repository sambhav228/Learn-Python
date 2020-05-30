'''Using Duck Typing for Dependency Injection, i.e. injecting an object to object of another class'''

class Flight:
    def __init__(self, engine):                     # Python allows us to pass any type of object, so it becomes easy for us to inject objects
        self.engine = engine                        # Here, we are doing Dependency Injection

    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")


class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")


ae = AirbusEngine()
f = Flight(ae)
f.startEngine()


be = BoeingEngine()
f1 = Flight(be)
f1.startEngine()