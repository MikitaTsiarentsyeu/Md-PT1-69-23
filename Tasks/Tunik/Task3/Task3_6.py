str = input("Please input your string whithout any punctuation mark and special symbols, you can use only space:\n")

vowels = ["e","y","u","i","o","a","E","Y","U","I","O","A"]


for i in vowels:
    for w in str:
        if i == w:
            str = str.replace(w,"")            
print(f"The string with all vowels removed:\n{str}")

