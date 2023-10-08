#4. Write a program that takes a list of numbers as input and 
#returns the second largest number in the list.

list_1=[345,234,2.07,45,302,-34,345,23.78,234,345,99,-3]

sort_list=sorted(list_1, reverse=True)
# Поскольку самое большое число может повторяться несколько раз - делаем проверку:
sec_number=sort_list[0]
for i in range(1, len(sort_list)):
    if sort_list[i]!=sort_list[0]:
        sec_number=sort_list[i]
        break

print(sec_number)