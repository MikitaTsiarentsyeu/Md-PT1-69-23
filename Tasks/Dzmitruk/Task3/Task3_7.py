# a program that takes a string as input and returns the string
# with all capital letters converted to lowercase and vice versa. 

text = input("Pleese, input a text: ")

# text = text.swapcase()
new_text = []

for letter in text:
    if letter == letter.lower():
        letter = letter.upper()
        new_text.append(letter)
    else:
        letter = letter.lower()
        new_text.append(letter)

new_text = ''.join(new_text)

print (new_text)


