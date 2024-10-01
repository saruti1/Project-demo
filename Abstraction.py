from abc import ABC,abstractmethod

class AbstractClass1(ABC):
    
    @abstractmethod
    def doSomething(self):
        print ("Some Implemetion in Parent class")

    def m1(self):
        print("This is sample Non-abstract Method")


class AnotherClass(AbstractClass1):
    def doSomething(self):
        super().doSomething()
        print ("Some Implemetion in Child class")

    def m2(self):
        print("This is a sample Method")


        
    
