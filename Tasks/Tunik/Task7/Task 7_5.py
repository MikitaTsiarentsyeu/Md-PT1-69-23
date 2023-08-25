def main(func): 
    dict = {}
    def wrapper(*args):
        if args[0] == "end":
            exit()
        if args[0] in dict:
            return dict[args[0]]
        values = func(args[0])
        dict[args[0]] = values
        return values
    return wrapper

@main
def lenght(word):
    return len(word)

flag = True
while flag:
    word = input("Input word to learn lenght of it:\n")
    result = lenght(word)
    print(f"Your lenght is - {result}")
    print("To close program print - end\n")
    if word == "end":
        flag = False




