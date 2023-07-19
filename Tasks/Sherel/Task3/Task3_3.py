"""3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string."""

user_input = input("Enter your string:\n")
user_input = user_input.replace(',', '').replace('.', '').replace(':', '').replace('!', '').replace('?', '').replace('-', '')
user_input = user_input.split()

myList = {}
for word in user_input:
    count_word = user_input.count(word)
    myList[word] = count_word

print(myList)