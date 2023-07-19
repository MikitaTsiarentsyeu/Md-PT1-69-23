"""5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters."""

user_input = input("Enter your string:\n")
user_input = user_input.replace(',', '').replace('.', '').replace(':', '').replace('!', '').replace('?', '').replace('-', '')
user_input = user_input.split()

myList = []
for i in user_input:
    length = len(i)
    if int(length) > 5:
        myList.append(i)

print("List with all strings that have a length greater than 5 characters:\n", myList)