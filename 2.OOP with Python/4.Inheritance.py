"""Inheritance are used to create a new class from an existing class. 
The new class is called the child class and the existing class is called the parent class. 
The child class inherits all the attributes and methods of the parent class."""

"""Suppose, phone is parent class and smartphone is child class.
 Smartphone will inherit all the attributes and methods of phone class."""

class Phone: #Parent class
    cat ="Electronics"
    def __init__(self,model,battery,camera):
        self.model=model
        self.battery=battery
        self.camera=camera
    
    #methods
    def charge(self,hours):
        self.charge=hours

class SmartPhone(Phone): #Child class
    def __init__(self,model,battery,camera,processor):
        super().__init__(model,battery,camera)
        self.processor=processor
       

#super is used to call the parent class constructor and methods.


Pro=SmartPhone("iPhone 12", 2815, "12MP", "A14 Bionic")
print(Pro.model)
print(Pro.battery)
Pro.charge(100) #child class can access parent class method.
print(Pro.charge)