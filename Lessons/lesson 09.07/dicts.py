d = {"one":[1], 2:"two"}
print(type(d), d)

# {[]:"test"} error

print(d["one"])
# print(d[100]) error

d[1] = "one"
print(d)
d[1] = 1.0
print(d)