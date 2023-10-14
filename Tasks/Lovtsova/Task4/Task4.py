# просим ввести длину и проверяем:

while True:
    line_num=input("Please, enter maximum number of characters per line, which must be greater than 35!\n")
    if not line_num.isdigit():
        print ("It's not correct data!\n\tPlease, try again!")
        continue
    line_num=int(line_num)
    if line_num<35:
        print ("Number  must  be  greater  than  35!\n\tPlease, try again!\n")
        continue
    break

# открфваем файл, читаем строки и создаем список списков слов в строках

with open("text.txt",'r', encoding="utf-8") as f, open(f"text_{line_num}_simb.txt",'w', encoding="utf-8") as formf:
    lines=f.readlines() #список исходных строк
    for line in lines:
        list_word=line[:-1].split(" ") #список слов вх.строки
        newline_len=0 #длина новой строки
        newline=[]    #создаем список новых подстрок
        for word in list_word:
            if newline_len+len(word)<=line_num-1:
                newline_len+=len(word)+1 #считаем новую длину строки
            else:
                newline[-1]=newline[-1][:-1] #последнее слово оставляем без пробела
                new_str="".join(newline)+"\n"
                k=line_num-len(new_str)
                while k!=0:
                    new_str=new_str.replace(' ','  ',k)
                    k=line_num-len(new_str)
                formf.write(new_str)
                newline_len=len(word)+1
                newline=[]   
            newline.append(word+" ") #добавляем следующее слово 
        new_str="".join(newline)+"\n"
        formf.write(new_str)
print(f'Formatting is complete! The result can be seen in the file: "text_{line_num}_simb.txt"')