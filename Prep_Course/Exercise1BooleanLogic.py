


# Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"

# Write a comment that says "This is a comment."
# This is a comment.

#Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

#Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 < 4:
    print("Math is fun.")

#Assign a variable called nope to an absence of value.
nope = None

#Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
True and False

#Calculate the length of the string "What's my length?"
str_Q = "What's my length?"
num = 0
for count in str_Q:
    num = num + 1
    
print(f"length is {num}")
str_len = len(str_Q)
print(f"length is {str_len}")

#Convert the string "i am shouting" to uppercase.
print("i am shouting".upper())

#Convert the string "1000"to the number 1000.
str_num = "1000"
int_num = int(str_num)

print(f"This {int_num} is type {type(int_num)}")

#Combine the number 4 with the string "real" to produce "4real".
str(4)
str_real = "real"
print(str(4) + str_real)

#Record the output of the expression 3 * "cool".
exp_1 = 3 * "cool"
print(exp_1)

#Record the output of the expression 1 / 0.
# exp_2 = 1 / 0 
try:
    result = 1 / 0
except ZeroDivisionError as e:
    result = str(e)  # result = "division by zero"
    print(result)
    
#Determine the type of [].
print(type([]))

#Ask the user for their name, and store it in a variable called name.
name = input("Enter your name:")

#Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.
ent_num = input("Enter a number:")
int_num = int(ent_num)
if int_num < 0:
    print("That number is less than 0!")
elif int_num > 0 :
    print("That number is greater than 0!")
else:
    print("You picked 0!")
    
#Find the index of "l" in "apple".
fruit = "apple"
for i in range(len(fruit)):
    if fruit[i] == "l":
        print(f"Index is {i}")
#another approach        
print("apple".index("l"))

#Check whether "y" is in "xylophone".
word = "xylophone"
for i in word:
    if i == "y":
        print(f"There is y in {word}")

y_found = word.find("z")
if y_found > 0 :
    print(f"Y is found in {word}")
    
#Check whether a string called my_string is all in lowercase.
str_check = "my_string"
if str_check.islower:
    print(f"all lowercase in {str_check}")
    




    
    