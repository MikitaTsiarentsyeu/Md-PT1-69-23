#1. Write a program that takes a string as input from a user and returns the number of vowels in the string.

import re

str_1=input('Please, input your string\n')
res=len(re.findall(r'[AaEeOoUuYyIiЕеУуОоАаЫыЁёЯяИиЮюэЭ]',str_1))
print(res)