import csv
from error import ErrorOccurance
class Item:
    all=[]
    pay_rate=0.8 # class attribute
    def __init__(self,name: str,price: int,quantity:int): #automatically runs when the object is created
        #assigning validations
        assert price >=0, f"Price is not equal or greater than 0: {price}"
        assert quantity>=0, f"quantity is not greater or equal to 0: {quantity}"
        
        
        #assigning attributes to objects
        self.__name=name
        self.__price=price
        self.quantity=quantity
        
        #filling class list each time the object created
        Item.all.append(self)
        
    @property#2
    def name(self): #calls the method as attribute
        print("This is reading property method")
        return self.__name
    
    @name.setter #setting new name
    def name(self,value):#1
        if len(value)>10:
            raise ErrorOccurance("Your value length is too long")
        else:
            self.__name=value
        
    def total_price(self):
        return self.price*self.quantity
    
    @property
    def price(self):
        return self.__price
    
    def discount_price(self,discount_value):
        self.__price= self.__price-self.__price*discount_value
        
    def increment_price(self,increment_value):
        self.__price=self.__price+self.__price*increment_value
    
        
    @classmethod
    def csv_instance(cls):
        with open("oop/oop tutorial/items.csv","r") as file:
            reader=csv.DictReader(file)
            items=list(reader)
            
           
            for item in items:
                Item(
                    name=item.get("name"),
                    price=int(item.get("price")),
                    quantity=int(item.get("quantity"))
                )

        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

class Phone(Item):
    all=[]
    def __init__(self, name: str, price: int, quantity: int,broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones=broken_phones
        assert broken_phones>=0, f"Broken Phones count {self.broken_phones} can't be negative"
        Phone.all.append(self)
        
Item.csv_instance()
print(Item.all[0].price)
# Item.all[0].discount_price(0.3)
# print(Item.all[0].price)
Item.all[0].increment_price(0.3)
print(Item.all[0].price)











# print(Item.all) #here __repr__ method is run by default

# print(Item.pay_rate)
# print(item1.pay_rate) #instance level -> class level
# print(Item.__dict__) #brings all the attributes of Item class
# print(item1.__dict__) #brings all the attributes of item1 object


