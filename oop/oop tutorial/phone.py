from item import Item
import csv

class Phone(Item):
    # all=[]
    def __init__(self, name: str, price: int, quantity: int,broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones=broken_phones
        assert broken_phones>=0, f"Broken Phones count {self.broken_phones} can't be negative"
        # Phone.all.append(self)
    
    @classmethod
    def csv_instance(cls):
        with open("oop/oop tutorial/phones.csv","r") as fphones:
            reader=csv.DictReader(fphones)
            phones=list(reader)
            for phone in phones:
                Phone(
                    name=phone.get("name"),
                    price=int(phone.get("price")),
                    quantity=int(phone.get("quantity")),
                    broken_phones=int(phone.get("broken_phones"))
                )