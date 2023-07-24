"""3. Write a program that takes a string as input and returns a dictionary
 with the count of each word in the string."""

from tests import cases

string = cases[0]
# string = input('Enter any string: ')
string = string.replace('.', '').replace('!', '').replace(',', '').replace('?', '').replace('—', '').replace('-', '').replace('_', '').replace('+', '').lower()

words = string.split()
my_dict = dict()
for word in words:
    if word not in my_dict:
        my_dict[word] = 1
        continue
    my_dict[word] += 1
print(my_dict)
