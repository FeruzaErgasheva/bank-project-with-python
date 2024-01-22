# mylist=[1,2,3,4,5,6]
# s=lambda *lst:sum(lst)
# result=s(*list)
# print(result)

mylist=[1,2,3,4,5,6]
# yangi=list(map(lambda son:son*2,mylist))
# print(yangi)
print(list(map(lambda son:son%2,mylist)))
