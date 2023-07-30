"""Write a program that takes a string as input
and returns a dictionary with the count of each word in the string"""

print("Here you can calculate the number of each word in your text")

text = input("Please, enter your text:\n")
text = text.replace('.', ''). replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').replace('-', '')
text = text.lower().split()

words = {}

for w in text:
    w_number = text.count(w)
    words[w] = w_number
print(f'The number of each word in your text:{words}')

