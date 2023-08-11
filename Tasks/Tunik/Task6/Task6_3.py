def count(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if (n1 == 0 or n1 < n2):
        return 0
    if (str1[0 : n2] == str2):
        return count(str1[1:],str2) + 1
    return count(str1[1:],str2)
print(count(str1 ="Hello World",str2="l"))
    
