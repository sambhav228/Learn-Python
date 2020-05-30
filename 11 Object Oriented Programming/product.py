'''This is my first class in python'''

class Product:
    def __init__(self):
        self.name = 'Dell Inspiron'
        self.description = 'Laptop, i7, 8th Gen, 8 GB RAM, 512 GB SSD'
        self.price = 91000

    def display(self):                          # Added an Instance function to print, so that we don't need to print each and every entity for every object separately
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()
p1.display()

# print(p1.name)
# print(p1.description)
# print(p1.price)


p2 = Product()
p2.display()
# print(p2.name)
# print(p2.description)
# print(p2.price)