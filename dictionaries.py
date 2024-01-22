# mydict={}
# # print(type(mydict))
# mydict={
#     "name":"Feruza",
#     "age":17,
#     "sname":"Ergasheva",
#     "major":"programmer"
# }
# for keys,values in mydict.items():
#     print(keys,values)




'''
people=[
    {
        "name":"Fayoza",
        "age":20
    },
    {
        "name":"Feruza",
        "age":18,
    },
    {
        "name":"Muslima",
        "age":12
    }

]
for x in range(1,len(people)+1):
    print(f"{x}-farzandning ismi {people[x-1]['name']}, yoshi {people[x-1]['age']}da")
'''

'''
dictionary->changeable,ordered,UNdupl

dictionary methods:
x=mydict.get("name")->Feruza
x=mydict.keys()->dict_keys(['name', 'age', 'sname', 'major'])
x=mydict.values()->dict_values(['Feruza', 17, 'Ergasheva', 'programmer'])
x=mydict.items()->dict_items([('name', 'Feruza'), ('age', 17), ('sname', 'Ergasheva'), ('major', 'programmer')])

change items:
mydict.update({'name':'Fayoza'})

remove items:
mydict.pop(key)
mydict.popitem()->last element
del mydict[key]
mydict.clear()


'''

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# nested_dict.setdefault('outer_key3', {})['inner_key5'] = 'another_new_value'
myfamily.setdefault("child4",{})['name']='Feruza'
print(myfamily)
