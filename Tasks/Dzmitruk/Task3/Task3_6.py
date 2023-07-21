# a program that takes a string as input
# and returns the string with all vowels removed.

vowels = "aeoui"
words = input("Please, input a string: ")
words = list(words)

for letter in words:
    if letter.lower() in vowels:
        words.remove(letter)

words = ''.join(words)
    
print (words)

        


