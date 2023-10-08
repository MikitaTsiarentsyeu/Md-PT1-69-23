#8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
#получаем список цифр и возвращаем среднее(есть встроенная функция - загуглить)

list_inp=[5,7,10,11,22,-43,5,7,10,11,22,43]

#import statistics
#average=round(statistics.mean(list_inp),4)


average=round((sum(list_inp)/len(list_inp)),4)

print(average)
