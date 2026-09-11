"""Abstractions are used to hide the internal details of a class
and only show the necessary features to the user."""

from abc import ABC, abstractmethod

class Telephone(ABC):   # abstract class

    @abstractmethod 
    def make_call(self):
        pass

    @abstractmethod
    def cap_photo(self):
        pass


class Sphone(Telephone): #child class that inherits from Telephone

    def make_call(self): #child class defining the abstract method
        print("Making a call from smartphone")

    def cap_photo(self): 
        print("Taking photo using smartphone camera")


# create object,we can't create telephone object because it's an abstract class
phone = Sphone()

phone.make_call()
phone.cap_photo()
"""This code shows abstraction where a base class defines required features 
and a child class provides their actual implementation."""