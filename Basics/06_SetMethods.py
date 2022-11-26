fruit = {"apple","banana","cherry","grapes","tomato"}
veg = {"drumstick","onion","tomato","chilly"}

#add
print(fruit)
fruit.add("kiwi")
print(fruit)

#remove
fruit.remove("cherry")
print(fruit)
#fruit.remove("cherry") #throws error
#print(fruit)

#discard
fruit.discard("cherry") # will not throw key error
print(fruit)

#pop
fruit.pop()
print(fruit)

#joining
#union
fruit.union(veg)
print(fruit)
print(veg)
union=fruit.union(veg)
print(union)

#update
fruit.update(veg)
print(fruit)

set1 = {1,2,3,4,5}
set2 = {1,2}
#intersection
set3 = set1.intersection(set2)
print(set1)
print(set3)
#
# #intersection-update
set1.intersection_update(set2)
print(set1)

set1 = {1,2,3,4,5}
#difference
set4 = set1.difference(set2)
print(set4)
set5 = set2.difference(set1)
print(set5)

#difference-update
set1.difference_update(set2)
print(set1)

#symmetric difference
set1 = {1,2,3,4,5}
set2 = {2,3,6,7,8,9}

set3 = set1.symmetric_difference(set2)
print(set3)

set1.symmetric_difference_update(set2)
print(set1)

set1={1,2,3,4,5}
set2={1,2}
print(set1.issuperset(set2))
print(set2.issubset(set1))