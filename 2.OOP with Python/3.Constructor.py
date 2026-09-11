#contructor is a special method in python which is used to initialize the object of a class. 
#It is defined using the __init__() method. 
#The __init__() method is called automatically when an object of a class is created. 
#It can take any number of arguments, but the first argument must be self, 
#which refers to the instance of the class.


class Phone:
    cat ="Electronics"
    def __init__(self,model,battery,camera):
        self.model=model
        self.battery=battery
        self.camera=camera
    
    #methods
    def charge(self,hours):
        self.charge=hours


Apple=Phone("Iphone 14",5000,"48MP")
print(Apple.model)
print(Apple.battery)
print(Apple.camera)
Apple.charge(100)
print(Apple.charge)
