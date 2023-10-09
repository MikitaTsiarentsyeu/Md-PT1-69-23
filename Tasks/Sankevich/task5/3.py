def more_than_5(list, better_list):
    print(list)
    for i in range(len(list)):
        list_item = list[i]
        if len(list_item) > 5:
            better_list.append(list_item)
        else:
            continue
    print(better_list)

bibs = []
random_words = []

while True:
    list_add_object = input('Incert string or print "!done": \n')
    if list_add_object == '!done':
        break
    else:
        random_words.append(list_add_object)



more_than_5(random_words, bibs)