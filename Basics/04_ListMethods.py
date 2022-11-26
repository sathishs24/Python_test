#append
fruits=["apple","orange","banana","berries"]
print(fruits)
fruits.append("kiwi")
print(fruits)

#insert
fruits.insert(2,"grapes")
print(fruits)

#remove
fruits.remove("grapes")
print(fruits)

#pop
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

#index
print(fruits.index("banana"))
print(fruits)

#count
fruits.append("orange")
print(fruits)
print(fruits.count("orange"))

#sort
fruits.sort()
print(fruits)

#reverse
fruits.reverse()
print(fruits)

#copy
newfruits = fruits.copy()
print(newfruits)

#clear
fruits.clear()
print(fruits)