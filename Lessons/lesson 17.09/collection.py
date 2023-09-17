class Collection:

    def __init__(self, *items) -> None:
        self.__items = []
        if items:
            self.__items.extend(items)

    def __str__(self) -> str:
        return f"{Collection.__name__}({','.join([str(x) for x in self.__items])})"
    
    def __len__(self):
        return len(self.__items)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Collection):
            return list(self) == list(__value)
        elif isinstance(__value, int):
            return len(self)==__value
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Collection):
            return Collection(list(self)+list(other))
        else:
            raise ValueError(f"Cannot add {type(other)} to a collection")

    def __iter__(self):
        self.__i = len(self)-1
        return self
    
    def __next__(self):
        if self.__i < 0:
            raise StopIteration
        val = self.__items[self.__i]
        self.__i -= 1
        return val

c = Collection(1,2,3,4,5)
print(c)

print(len(c))

print(c == 5)
print(c == Collection(1,2,3,4,5))
print(c == Collection())

for item in c:
    print(item)

print(list(c))

print(Collection(1,2,3)+Collection(4,5,6))
print(Collection(1,2,3)+6)