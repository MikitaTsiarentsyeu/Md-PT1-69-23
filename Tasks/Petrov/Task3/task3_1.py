string = input("Input a string: ")
vowels = "eyuioa"
count = 0
for char in string.lower():
    if char in vowels:
        count += 1
print(f"Number of vowels in your string is {count}")
