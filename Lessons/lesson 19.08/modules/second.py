test = "test"

lst = [1,2,3,4,5]

def func():
    lst.append(lst[-1]+1)

def print_test():
    print(test)

if __name__ == "__main__":
    print(f"hello from {__name__}!")

# __all__ = ['test']