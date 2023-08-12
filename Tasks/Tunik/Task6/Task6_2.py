def palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False
text = "Do geese see God"
text = text.lower().replace(" ","") 
if(palindrome(text)==True):
    print(f"{text} - String is a palindrome!")
else:
    print(f"{text} - String isn't a palindrome!")

text_two = "ExaMple fOr chEck"
text_two = text_two.lower().replace(" ","") 
if(palindrome(text_two)==True):
    print(f"{text_two} - String is a palindrome!")
else:
    print(f"{text_two} - String isn't a palindrome!")