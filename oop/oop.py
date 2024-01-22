# class Talaba:
#     def __init__(self,ism,familya,baho):
#         self.ism=ism
#         self.familya=familya
#         self.baho=baho

# talaba1=Talaba("Feruza","Ergasheva",5)
# talaba2=Talaba("Mayram","Bazarova",4)
# talaba3=Talaba("Fayoza","Ergasheva",3)

# min_of_three = lambda x, y, z: x if x.baho < y.baho and x.baho < z.baho else y if y.baho < z.baho else z
# print(min_of_three(talaba1, talaba2, talaba3))

class Talaba:
    def __init__(self, ism, familya, baho):
        self.ism = ism
        self.familya = familya
        self.baho = baho

talaba1 = Talaba("Feruza", "Ergasheva", 2)
talaba2 = Talaba("Mayram", "Bazarova", 4)
talaba3 = Talaba("Fayoza", "Ergasheva", 3)


min_of_three=lambda x,y,z:min(x,y,z, key=lambda talaba:talaba.baho)
print(min_of_three(talaba1,talaba2,talaba3).familya,min_of_three(talaba1,talaba2,talaba3).ism)
     