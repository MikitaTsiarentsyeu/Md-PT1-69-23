x = 5
print(x, repr(x), type(x))
x = str(x)
print(x, repr(x), type(x))

x = "test"
print(repr(x))

print("some very long string" == 'some very long string')

print(repr("test 'test' \" test"))

print('test "test" test')

'''test str'''
"""test str"""

lines = """      line1
    line2
    line3"""

print(repr(lines))

print("\t\\t\\est\t\\t\\est")
print(r"\t\\t\\est\t\\t\\est")

print(type("a"), type(" "), type(""))

print(len(""))
print(len("a"))
print(len(" "))
print(len("test"))

s = "my very long string"
print(s[0], s[1], s[2])
print(s[-1], s[-2], s[-3])

first_s = s[0]
print(len(first_s), first_s)

print(s[0:7])
print(s[0:len(s)])
print(s[:])
print(s[:9])
print(s[6:])

print(s[3:-3])
print(s[3:-3:3])

print(s[::-1])

print(s)

s = "TeSt StRiNg"
print(s.upper(), s)
print(s.lower(), s)

s = s.lower()
print(s)

print("test" in s)
print(" " in s)
print(ord("a"), ord("A"))
print("T" in s)
print("t" in s)
print("T" in s or "t" in s)

print(s.find("u"))

# s[0:4] = "TEST" error

s = s.replace('t', "TTT").replace(" ", '-')
print(s)

s = "test" + " " + "string"
print(s)

s = "NaNa"*8 + ", Batman!"
print(s)

s = "some very long string"
print(s.split("o"))

sku = "45354-65465-4545/45"
res = sku.split('-')

sku = "_".join(res)
print(sku)

print(" !!test!".strip('!'))