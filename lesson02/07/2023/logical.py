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
