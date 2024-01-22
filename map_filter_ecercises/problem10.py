lst=[1,2,3,4.15,6.24,15,34,2.23,3.34,4.96,24,35,67,21.23]
func=lambda x:  int(x) if isinstance(x,float) else float(x)
yangi=list(map(func,lst))
print(lst)
print(yangi)