def reversed_string(text):
    if len(text) == 1:
        return text
    return f"{reversed_string(text[-1])}{reversed_string(text[:-1])}"


line = input("Input text: ")
if line:
    print(reversed_string(line))
else:
    print("No text - no reverse text")
