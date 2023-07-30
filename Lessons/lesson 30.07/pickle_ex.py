import pickle

with open("print.pickle", 'wb') as f:
    pickle.dump(print, f)


with open("print.pickle", 'rb') as f:
    new_print = pickle.load(f)

print(new_print)

new_print("hello from new print")

with open("data.txt", "r") as f:
    data = eval(f.read())

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data = pickle.load(f)

print(data)