string = input("Input a string: ")
vowels = "eyuioa"
count = 0
for vowel in vowels:
    if vowel in string:
        string = string.replace(vowel, "")
    elif vowel.upper() in string:
        string = string.replace(vowel.upper(), "")
print(string)
