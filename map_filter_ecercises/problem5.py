from random import *
from math import *
n=int(input())
lst=[randint(1,100) for _ in range(10)]
func=lambda son:True if son>pow(n,3) else False
yangi=list(filter(func,lst))
print(lst)
print(yangi)
