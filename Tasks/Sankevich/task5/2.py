def reverse_list(list):
    print(list)
    for i in range(len(list)):
        list_element = list[i]
        list_element = list_element[::-1]
        list[i] = list_element
    print(list)

list1 = []

while True:
    list_add_object = input('Incert string or print "!done": \n')
    if list_add_object == '!done':
        break
    else:
        list1.append(list_add_object)

reverse_list(list1)