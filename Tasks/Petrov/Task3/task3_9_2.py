string = input("Input a string: ")
new_string = ""
for char in string:
    new_string = f"{char}{new_string}"
print(f"Reversed string: {new_string}")
