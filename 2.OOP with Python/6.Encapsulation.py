"""Encapsulations are used to hide the data from outside world 
and only allow access through methods.
This is done to protect the data from unauthorized access 
and to ensure that the data is accessed in a controlled manner."""

class Student:
    def __init__(self, name, cgpa):
        self.name = name        # public
        self.__cgpa = cgpa      # private (hidden)

    def get_cgpa(self): #with this method we can access the private variable
         return self.__cgpa

    def set_cgpa(self, value): #with this method we can modify the private variable
        if value >= 3 and value <= 4:
            self.__cgpa = value
        else:
            print("Invalid CGPA")

# create object
s = Student("Asir", 2)

# access using method
print(s.get_cgpa())

# modify using method
s.set_cgpa(3.8)
print(s.get_cgpa())

#s.cgpa(4.00), direct access to private variable will result in error




