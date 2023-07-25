# a program that takes a list of strings as input and returns a list
# with all strings that have a length greater than 5 characters.

text = input("Please, input a list of strings: ")

text = list(text.split(", "))

strings = []

for words in text:
    
    if len(words) > 5:
        strings.append(words)
    
print(strings)



    
    
