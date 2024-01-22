# def add(son: int)->int:
#     return son+10
# mylist=list(range(10))
# print(mylist)
# print(list(map(add,mylist)))

# def intro(*lst):
#     print(f'hello {lst[1]}')

# lst=['Feruza','Fayoza','Muslima']
# intro(*lst)

def names(**ismlar):
    print(ismlar['first'])

names(first="Fayoza",second="Feruza")
