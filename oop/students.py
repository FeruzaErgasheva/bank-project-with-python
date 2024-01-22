import csv
class Students:
    all=[]
    def __init__(self,name:str,surname:str,age:int,major:str):
        assert age>=0, f"Age can't be negative:{self.age}"
        
        self.name=name
        self.surname=surname
        self.age=age
        self.major=major
        Students.all.append(self)
        
    @classmethod
    def csv_students(cls):
        with open("oop/students.csv","r") as file:
            reader=csv.DictReader(file)
            students=list(reader)
            
            for student in students:
                print(student)
                Students(
                    name=student.get("name"),
                    surname=student.get("surname"),
                    age=int(student.get("age")),
                    major=student.get("major")
                )
                  
    def __repr__(self):
        return f"Student:('{self.name}','{self.surname}', {self.age}, '{self.major}')"
    
Students.csv_students()
# print(Students.all)