# a program that takes a string as input from a user
# and returns the number of vowels in the string.

vowels = "aeoui"
words = input("Please, input a string: ")
words = list(words)

found = {}

for letter in words:
    if letter.lower() in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in found.items():
    print(k, "was foud", v, "time(s).")

        
        


