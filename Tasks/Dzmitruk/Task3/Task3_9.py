# a program that takes a string as input and returns the string reversed.

text = input("Pleese, input a string: ")

# text = text[::-1]

new_text = []

for letter in text[::-1]:
    new_text.append(letter)

new_text = ''.join(new_text)

print ("The string reversed is:", new_text)

        


