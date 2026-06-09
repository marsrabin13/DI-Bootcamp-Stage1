# A dictionary is a collection of key-value pairs. Each key is associated with a value, and you can use the key to access the value. Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. The key and value are separated by a colon.
authors = {
    'Great Gatsby': 'F. Scott Fitzgerald',
    'Slaughterhouse Five': 'Kurt Vonnegut',
    'Of Mice and Men': 'John Steinbeck'
}

print(authors['Great Gatsby'])

#dict() is a built-in function that creates a new dictionary. You can use it to create an empty dictionary or to create a dictionary from a list of key-value pairs.
user_info = dict(name = 'John')
print(user_info)  # {'name': 'John'}
print(user_info['name'])  # 'John'

#modify and add new key-value pairs to the dictionary
user_info['name'] = 'Dan' #modify the key that exists
user_info['email'] = 'dan@gmail.com' #creates a new key with a value
print(user_info)  # {'name': 'Dan', 'email': 'dan@gmail.com'}

#copy() is a method that creates a shallow copy of the dictionary. This means that it creates a new dictionary with the same key-value pairs, but if the values are mutable objects (like lists or other dictionaries), they will be shared between the original and the copy.
user_info = dict(name='Alice', age=30, city='New York')
user_info_copy = user_info.copy()
print(user_info_copy)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

#fromkeys() used to initialize a dictionary with default values for a list of keys. It takes two arguments: the first is a list of keys, and the second is the default value that will be assigned to each key.
users = ['Alice', 'Bob', 'Charlie']
user_status = {}.fromkeys(users, "inactive")
print(user_status)  # {'Alice': 'inactive

#get() is a method that returns the value for a specified key if the key is in the dictionary. If the key is not found, it returns a default value (which is None if not specified).
user_info = {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
print(user_info.get('city'))  # Los Angeles
print(user_info.get('country', 'Canada'))  # USA (default value since 'country' key is not in the dictionary)

#items() is a method that returns a view object that displays a list of dictionary's key-value tuple pairs.
user_info = dict(name='Alice', age=30, city='New York')
print(user_info.items())

#keys() is a method that returns a view object that displays a list of all the keys in the dictionary.
user_info = dict(name='Alice', age=30, city='New York')
print(user_info.keys())

#pop() is a method that removes a specified key and returns the corresponding value. If the key is not found, it returns a default value (which is None if not specified).
user_info = dict(name='Alice', age=30, city='New York')
print(user_info.pop('age'))  # 30
print(user_info)  # {'name': 'Alice', 'city': 'New York'}

#popitem() is a method that removes and returns an arbitrary key-value pair from the dictionary. If the dictionary is empty, it raises a KeyError.
user_info = dict(name='Alice', age=30, city='New York')
print(user_info.popitem()) 
print(user_info)  # The remaining key-value pairs in the dictionary

#update() Updates the dictionary with key-value pairs from another dictionary or iterable:
user_info = dict(name='Alice', age=30, city='New York')
additional_info = {'country': 'USA', 'email': 'alice@example.com'}
user_info.update(additional_info)
print(user_info)  