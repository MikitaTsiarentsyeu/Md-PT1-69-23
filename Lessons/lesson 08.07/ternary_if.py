name = "test"

if name:
    print("hello,", name)
else:
    print("hello!")

print("hello,", name) if name else print("hello!")

print("hello, "+name if name else "hello")

res = "hello, "+name if name else "hello"
print(res)


if new_var:= 10:
    print(new_var)