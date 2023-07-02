import math
x=True
print(x, type(x))

res= 1 == True
print(res)


print (id(1), id(True)) #id не понятно
print(1 is True) #is не понятно


print(isinstance(True,bool))
print(isinstance(True,float))
print(isinstance(True,int))

print((5+True)*False)

number=-5
print(number >0)
#print (number <100)
#print(0<number<100)


print(bool(100))
print(bool(-math.inf))
print(bool(math.nan))


#логические выражения
print (not not not True)
print (not"0")

print (number >0 and number< 100)

print (5 and 6)

print(0 and 6)

print("left") or print ("right")
print("left") and print ("right")
