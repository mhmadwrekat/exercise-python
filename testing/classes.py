
"""
Classes 
"""
from abc import ABC , abstractmethod

def view():
    print('------------------------------------------------------')

class Pet:
    conut = 0
    # Constructor Mehod
    def __init__(self, name , age):
        self.name = name
        self.age = age
        Pet.conut += 1

    # Instance method (Default)
    def greet(self):
        return f'hello my name is {self.name} , I am {self.age} Months .'    
    # Decorator
    @abstractmethod
    def speak(self):
        return 'This is a pet'
    @classmethod
    def petCount(cls):
        return cls.conut

class Cat(Pet) :
    def __init__(self , name , age , hair) :
        super().__init__(name , age)
        self.hair = hair
    
    def __repr__(self):
        return f'{self.name} : CAT'

    def speak(self):
        if self.hair:
            return 'Meaoooowwww , I Have Hair'
        else :
            return 'Meaoooowwww , I Dont Have Hair'
 
class Dog(Pet) :
    def speak(self):
        return 'Whoooooofff'
    @staticmethod
    def averageAge():
        return 7
    
    def __str__(self):
        return f'{self.name} : DOG'

class Rabbit(Pet):
    pass

if __name__ =="__main__":
    # Instatiation
    oscar = Dog('Oscar', 4)
    snowy = Cat('Snowy' , 8 , True)
    Whity = Rabbit('Whity', 22)
    view()
    print(snowy.greet())
    print(snowy.speak())
    print(oscar.greet())
    print(oscar.speak())
    print(Whity.greet())
    print(Whity.speak())
    view()
    print('Static Method')
    print(f'average Age for Dogs is {oscar.averageAge()} Months .\nOr U Can Use {Dog.averageAge()} Months .')
    view()
    print(f'You Have | {Pet.petCount()} | Used ')
    view()
    print(type(oscar))
    print(oscar)
    print(snowy)
    print(Whity)
    view()

"""
End Of Classes
"""