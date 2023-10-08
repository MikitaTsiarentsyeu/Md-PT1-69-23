#5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

list_input=["sdfvbnl","h","fuluihiujh","d","ds","nsuelgr"]
res=[]
for i in list_input:
    if len(i)>5:
        res.append(i)
print(res)