from random import *

class Bino:
    def __init__(self,rang,balandlik):
        self.rang=rang
        self.balandlik=balandlik
bino1=Bino("qizil",randint(1,100))
bino2=Bino("oq",randint(1,100))
bino3=Bino("yashil",randint(1,100))
bino4=Bino("ko'k",randint(1,100))
bino5=Bino("sariq",randint(1,100))

bino_list=[bino1,bino2,bino3,bino4,bino5]
func=lambda x:True if x.balandlik>50 else False
mylist=list(filter(func,bino_list))

for building in range (len(mylist)):
    print(mylist[building].rang, mylist[building].balandlik)
