def count_lowercase_uppercase_chars(input_string):
    lowercase_count = 0
    uppercase_count = 0
    
    for char in input_string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
    
    return lowercase_count, uppercase_count

text = "Hello World!"
lowercase, uppercase = count_lowercase_uppercase_chars(text)
print("Символов нижнего регистра:", lowercase)
print("Символов верхнего регистра:", uppercase)
