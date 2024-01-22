import csv
class Family_members:
    all=[]
    def __init__(self,name:str,surname:str,age:int,education:str,marital_status:bool) :
        assert age>=0, f"Age can't be negative:{self.age}"
        self.name=name
        self.surname=surname
        self.age=age
        self.education=education
        self.marital_status=marital_status
        
        Family_members.all.append(self)
    
    @classmethod
    def csv_instances(cls):
        with open("oop/family.csv","r") as file:
            reader=csv.DictReader(file)
            members=list(reader)
            
            for member in members:
                Family_members(
                    name=member.get("name"),
                    surname=member.get("surname"),
                    age=int(member.get("age")),
                    education=member.get("education"),
                    marital_status=member.get("marital_status").lower() == "true"  # Convert to boolean
                )
                
    def __repr__(self):
        return f"Member('{self.name}','{self.surname}',{self.age},'{self.education}',{self.marital_status})"


Family_members.csv_instances()
married_people=list(filter(lambda member:member.marital_status,Family_members.all))
print(married_people)
        
        