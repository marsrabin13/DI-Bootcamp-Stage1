fav_fruits = ("strawberry", "banana", "grape")
print(fav_fruits[0])  # Output: strawberry
print(fav_fruits.count("banana"))  # Output: 1
print(fav_fruits.index("grape"))  # Output: 2


numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

numbers.clear()
print(numbers)  # Output: set()

numbers = {1, 2, 3, 4, 5}
prime_num = {2, 3, 5, 7, 11}
print(numbers.intersection(prime_num))  # Output: {2, 3, 5}



