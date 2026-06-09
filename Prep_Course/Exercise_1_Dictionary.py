#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).
list1 = [("name", "Elie"), ("job", "Instructor")]
dictionary1 = dict(list1)
print(dictionary1)


#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
state_initial = ["CA", "NJ", "RI"]
state_name = ["California", "New Jersey", "Rhode Island"]
dictionary2 = {}
for i in range(len(state_initial)):
    dictionary2[state_initial[i]] = state_name[i]
print(dictionary2)


#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = 'aeiou'
dictionary3 = {}
for letter in vowels:
    dictionary3[letter] = 0
print(dictionary3)

#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:
import string 
dictionary4 = {}
alpha_list = list(string.ascii_uppercase)
for i in range(len(alpha_list)):
    dictionary4[i+1] = alpha_list[i]
print(dictionary4)

#Bonus: 
'''Given the string "awesome sauce", return a dictionary where the keys are vowels, 
and the values are the count of each vowel in the string. Your dictionary should look like 
this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.
'''
vowels = 'aeiou'
str2= "awesome sauce"
dictionary5 = {}
for letter in vowels:
    dictionary5[letter] = str2.count(letter)
print(dictionary5)
