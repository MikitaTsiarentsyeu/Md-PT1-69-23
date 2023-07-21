"""7. Write a program that takes a string as input and returns the string
 with all capital letters converted to lowercase and vice versa."""
string = 'HellO! My FriEnd !@12'
#string = input('Enter any string: ')
ans = []

for s in string:
    if s.isalpha():
        if s.islower():
            ans.append(s.upper())
            continue
        ans.append(s.lower())
        continue
    ans.append(s)

print(string)
print(''.join(ans))
# Also, using swapcase():
print(string.swapcase())



