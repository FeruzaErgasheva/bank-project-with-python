import csv
class Item:
    all=[]
    pay_rate=0.8 # class attribute
    def __init__(self,name: str,price: int,quantity:int): #automatically runs when the object is created
        #assigning validations
        assert price >=0, f"Price is not equal or greater than 0: {price}"
        assert quantity>=0, f"quantity is not greater or equal to 0: {quantity}"
        
        
        #assigning attributes to objects
        self.__name=name
        self.price=price
        self.quantity=quantity
        
        #filling class list each time the object created
        Item.all.append(self)
    @property
    def name(self):
        return self.__name
        
    def total_price(self):
        return self.price*self.quantity
    
    def discount_price(self):
        self.price= self.price*self.pay_rate
        
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