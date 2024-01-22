from random import *
from math import *
lst=[uniform(1,100) for _ in range(10)]

lst1=list(map(lambda son:ceil(son),lst))
print(lst)
print(lst1)