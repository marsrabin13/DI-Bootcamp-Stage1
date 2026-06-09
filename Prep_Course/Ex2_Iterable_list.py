fruits = ["apple", "banana","cherry","date","elderberry"]

fruits.append("fig")
print(fruits)

fruits.insert(0,"grape")
print(fruits)


fruits.remove("cherry")
print(fruits)

fruits.pop()
print(fruits)

berries = ["strawberry","blueberry"]
combined_list = fruits.copy()
combined_list.extend(berries)
print(combined_list)

combined_list.sort()
print(combined_list)

print(combined_list[-3:])