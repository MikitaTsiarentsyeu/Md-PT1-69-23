# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

user_input = input("Enter the string: ")
word_list = user_input.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Number of each word in a line:", word_count)