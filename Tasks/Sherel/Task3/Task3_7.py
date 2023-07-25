"""7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa."""

user_input = input("Enter your string:\n")

myList = ""
for i in user_input:
     if i.isupper():
         myList += i.lower()
     else:
          myList += i.upper()

print(myList)