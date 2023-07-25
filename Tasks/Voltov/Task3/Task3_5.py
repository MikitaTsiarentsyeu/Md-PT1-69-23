# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.


user_input = input("Enter a comma-separated list of strings: ")
str_list = user_input.split(",")
long_str_list = []
for string in str_list:
    if len(string) > 5:
        long_str_list.append(string)
print("Strings longer than 5 characters:", long_str_list)