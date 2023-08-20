import back

def start():
    while True:
        ch = input("""Choose a point of menu:
            0.exit
            1.show all products
            2.add a product
            3.remove a product
            4.search by name\n""")
        if ch == '1':
            show_all()
        elif ch == '2':
            add_product()
        elif ch == '3':
            remove_product()
        elif ch == '4':
            search()
        elif ch == '0':
            print("Good buy!")
            break


def show_all():
    res = back.show_all()
    print(res)

def add_product():
    values = []
    for attr in back.attrs:
        value = enter_value_by_key(attr)
        values.append(value)
    res = back.add_product(*values)
    if res:
        print("the product was added")
    else:
        print("the product name is already in use")
    
def remove_product():
    value = enter_value_by_key(back.attrs[0])
    res = back.remove_product(value)
    if res:
        print("the product was removed")
    else:
        print("nothing was found")

def search():
    value = enter_value_by_key(back.attrs[0])
    res = back.search(value)
    if res:
        print(res)
    else:
        print("nothing was found")


def enter_value_by_key(key):
    return input(f"please enter product {key}\n")