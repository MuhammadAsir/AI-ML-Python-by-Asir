"""Multiple Inheritance: A class can inherit from multiple classes, 
allowing it to combine the features and behaviors of all the parent classes. 
This promotes code reuse and allows for more complex and versatile class designs."""

class Phone: 
    cat ="Electronics"
    def __init__(self,model,battery,camera):
        self.model=model
        self.battery=battery
        self.camera=camera
    
    #methods
    def charge(self,hours):
        self.charge=hours

class Cooling_System: 
    def __init__(self,cooling_method):
        self.cooling_method=cooling_method

    def cool(self):
        print(f"Cooling the phone using {self.cooling_method}")   
            

class SmartPhone(Phone): 
    def __init__(self,model,battery,camera,processor):
        super().__init__(model,battery,camera)
        self.processor=processor

class Smartphone_CoolingMode(SmartPhone,Cooling_System):
    def __init__(self,model,battery,camera,processor,cooling_method):
        SmartPhone.__init__(self,model,battery,camera,processor)
        Cooling_System.__init__(self,cooling_method)
       

Pro=Smartphone_CoolingMode("iPhone 17", 3000, "50MP", "A14 Bionic","Liquid Cooling")
print(Pro.model)
print(Pro.cooling_method)
Pro.cool()
print(Pro.processor)
print(Pro.battery)
Pro.charge(100)
print(Pro.charge)




