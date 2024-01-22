lst=[1,2,3,4.15,6.24,15,34,2.23,3.34,4.96,24,35,67,21.23]
func=lambda x:True if isinstance(x,int) else False
yangi=list(filter(func,lst))
print(lst)
print(yangi)