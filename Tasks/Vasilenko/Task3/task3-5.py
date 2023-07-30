"""Write a program that takes a list of strings as input
and returns a list with all strings that have a length greater than 5 characters"""

print("Here you can find out which words in your text have more than 5 characters")

text = input("Please, enter your text:\n")
text = text.replace('.', ''). replace(',', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').replace('-', '')
text = text.lower().split()

new_list =[]

for w in text:
    if len(w) > 5:
        new_list.append(w)

print(f'All of your words that have more than 5 characters:{new_list}')

