#6. Write a program that takes a string as input and returns the string with all vowels removed.


import re

str_1=input('Please, input your string\n')
res=re.sub(r'[AaEeOoUuYyIiЕеУуОоАаЫыЁёЯяИиЮюэЭ]','',str_1)
print(res)
