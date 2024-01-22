from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,name:str,price:float,color:str) -> None:
       self.name=name
       self.price=price
       self.color=color
    
    @abstractmethod
    def changePrice(self,newPrice:float):
       pass
    @abstractmethod
    def __str__(self) -> str:
        pass
    
class Car(Vehicle):
    def changePrice(self, newPrice: float):
        self.price=newPrice
    def __str__(self) -> str:
        return f"""
    name:{self.name}
    price:{self.price}
    color:{self.color}
    """

car1=Car("Matiz",5_000,"black")
print(car1)