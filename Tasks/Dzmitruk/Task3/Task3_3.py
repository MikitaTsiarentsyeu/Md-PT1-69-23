# a program that takes a string as input
# and returns a dictionary with the count of each word in the string

count = {}

text = input("Please, input a text: ")

text = text.replace(".", "" )
text = text.replace(",", "" )
text = text.replace("!", "" )
text = text.replace("-", "" )
text = text.replace("?", "" )
text = list(text.split(" "))

i = 0

for word in text:
    i += 1
    word = word.lower() 
    count.setdefault(word, 0)
    count[word] += 1
   
for k, v in count.items():
    print(f"Word '{k}' was found {v} time(s).")
    
