str = input("Please input your string whithout any punctuation mark and special symbols, you can use only space:\n")

str = str.replace(" ",'')

vowels = ["e","y","u","i","o","a","E","Y","U","I","O","A"]

number = 0

for i in vowels:
    for w in str:
        if i == w:
            number +=1
print(f"The number of vowels in the string - {number}")


