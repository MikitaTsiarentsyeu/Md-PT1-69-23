"""3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string."""

user_input = input("Enter your string:\n")
rep = ",.:;!?-#@$%^&*()_+|/"
user_input = ''.join([x for x in user_input if x not in rep]) #add comprehensions from lessons 22.07
user_input = user_input.split()

myList = {}
for word in user_input:
    count_word = user_input.count(word)
    myList[word] = count_word

print(myList)