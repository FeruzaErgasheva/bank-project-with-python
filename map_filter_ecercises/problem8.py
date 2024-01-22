lst=["b","a","street",1,2,3,True,'random',"1",1.23,"olma"]
func=lambda variable: True if isinstance(variable,str) else False
yangi=list(filter(func,lst))
print(lst)
print(yangi)