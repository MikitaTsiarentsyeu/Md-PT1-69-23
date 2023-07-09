c, d, p = "cat", "dog", "parrot"

"a cat, a dog and a parrot"

res = "a " + c + ", a " + d + " and a " + p
print(res)

"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

pattern = "a {2}, a {1} and a {0}"

print(pattern.format(c, d, p))

print(f"test str {d if d else c}")

print(f"a {c}, a {d} and a {p}")


s = "1 2 3"
# s = s+" 4"
s = f"{s} 4"
