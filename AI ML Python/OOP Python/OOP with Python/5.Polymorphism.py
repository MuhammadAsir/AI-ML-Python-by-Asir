"""In short Polymorphism allows us to use a single interface to represent 
different types of objects."""

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin:
    def fly(self):
        print("Penguin cannot fly")

# create objects
b = Bird()
p = Penguin()

# same method call, different behavior
b.fly()
p.fly()