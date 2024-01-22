myset=set()
thisset={"apple","banana","cherry"}
set1=set((1,2,3,4,5))
set2={"apple","banana","cherry","ant","Air","Airplane"}

_=[print(x.lower(),end=" ") for x in set2 if x.lower().startswith("a")]

# print(f"myset{type(myset)}\nthisset:{type(thisset)}\nset1:{type(set1)}")

'''
sets->unordered,unchangeable,undupl

set change methods:
set.add(item)
myset.update(sequence)
myset.remove(item)->raises error if item is not available
myset.discard(item)->doesn't raise error if item is not available
myset.pop()->removes random item
myset.clear()->empties set
del myset ->deletes the set

set join methods:
set3=set1.union(set2)->new set containing all elements
set1.update(set2)
set1.intersection_update(set2)->keeps elements if available in both sets (set3=set1.intersection(set2))
set1.symmetric_difference_update(set2)->keeps all elements but not duplicates(set3=set1.symmetric_difference(set2))
newset=set1.copy()
set1.difference_update(set2)->removes element of set1 if they are same with those at set2(difference)
x=set1.isdisjoint(set2) ->if intersection is empty(True), otherwise False



'''