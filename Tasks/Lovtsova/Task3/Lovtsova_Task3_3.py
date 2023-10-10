#3. Write a program that takes a string as input and 
#returns a dictionary with the count of each word in the string.

import re

str_1=input('Please, input your string\n')


# убираем знаки препинания и иные похожие символы из строки и сплитуем в список по пробелу

list_str=(re.sub(r"[.,!?:;-=+-_*/#'№~%)(]","",str_1)).split(' ')

#формируем словарь:
d={}
for i in list_str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

# делаем красивый вывод:
for key in d:
    print(f'*{key}* встречается {d[key]} раз(a)')