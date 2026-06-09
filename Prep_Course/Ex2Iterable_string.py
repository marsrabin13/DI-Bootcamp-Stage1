user_input = input("Input a sentence:")

if user_input.isalpha():
    print("sentence is alphabetic")
else:
    count_alpa = 0
    for char in user_input:
        if char.isalpha():
            count_alpa += 1
    print("Number of alphabets in the sentence:", count_alpa)   
    
if user_input.endswith("!"):
    print("sentence ends with !")
else:
    print("sentence does not end with !")
    
for char in user_input:
        if char.isspace():
            print("Sentence has white space")
            space_not_found = False
            break
        else:
            space_not_found = True

if space_not_found:
    print("Sentence has NO white space")
        

    