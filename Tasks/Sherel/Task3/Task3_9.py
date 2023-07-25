"""9. Write a program that takes a string as input and returns the string reversed."""

# #the first var
# user_input = input("Enter your string:\n")
# print(user_input[::-1])

#the second var
user_input = input("Enter your string:\n")

myList_revers = ""
for i in user_input:
    myList_revers = i + myList_revers

print(myList_revers)
