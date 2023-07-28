user = input("Enter a maximum number of characters per line:\n")
if not user.isdigit():
    print("Please enter correct data")
    exit()
sentence_limit = int(user)
if sentence_limit <= 35:
    print("Please enter number greater than 35")
    exit()
with open("text.txt","r",encoding='utf-8') as t, open("ready_text.txt","w",encoding='utf-8') as rt:
    data = t.read()
    buffer = ""
    space = " "
    list_of_sentence = []
    for word in data.split():
        word_length = len(word)
        buffer_length = len(buffer)
        if buffer_length + word_length < sentence_limit:
            if buffer:
                buffer += space
            buffer += word        
        else:
            list_of_sentence.append(buffer)
            buffer = word
    list_of_sentence.append(buffer)    
    for x,i in enumerate(list_of_sentence):
        l = len(i)
        if l == sentence_limit:
            continue
        index = [w for w,index in enumerate(i) if index == space]
        z = 0
        zero = 0
        one = 1
        key = 1
        while z != sentence_limit:
            for place in index:
                new = f"{i[:(place+one)]}{i[place+zero:]}"
                i = new
                one+=1
                zero+=1
                key = 1
                z = len(new)
                if z == sentence_limit:
                    list_of_sentence[x] = new
                    zero = 0
                    one = 1
                    break
                if place == index[-1]:
                    index = [w for w,index in enumerate(new) if index == space]
                    zero = 0
                    one = 1
                    key = 1            
                    for g in index:
                        a = index[key]
                        if g+1 == a:
                            index.remove(g)
                            key += 1
    n = "\n".join(list_of_sentence)
    rt.write(n)        



            


