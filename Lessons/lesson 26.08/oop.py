from typing import Any


class Dog:

    name = ""
    breed = ""
    color = ""

    def woof(self):
        if self.breed == "shepherd":
            print("Woooooof!")
        else:
            print("woof!")

print(Dog, type(Dog))
print(repr(Dog.name))

Dog.name = "TEST NAME"
print(repr(Dog.name))

new_dog = Dog()
print(new_dog.name)
print(new_dog.breed)
print(new_dog.color)

print(type(new_dog))

new_dog.name = "Max"
new_dog.breed = "shepherd"
new_dog.color = "black"

print(new_dog.breed)

Dog.name = ""
print(new_dog.name)

zefirka = Dog()
print(zefirka.name)
zefirka.name = "Zefirka"
zefirka.breed = "wss"
zefirka.color = "white"

print(new_dog.breed, zefirka.breed)

zefirka.woof()
new_dog.woof()


# Monkey patching

Dog.weight = 100
print(Dog.weight)

print(zefirka.weight)
print(new_dog.weight)

zefirka.weight = 35
print(zefirka.weight)

zefirka.favorite_toy = "red ball"
print(zefirka.favorite_toy)

# def play(self):
#     print(f"playing with {self.favorite_toy}")

# zefirka.play = play
# zefirka.play(zefirka)

hasattr(zefirka, "breed")

print(zefirka.__getattribute__("breed"))
zefirka.breed = ""
zefirka.__setattr__("breed", "")

print(zefirka.__dict__)
print(new_dog.__dict__)

print(new_dog.weight)

# new_dog.__getattribute__("weight")

print(hasattr(new_dog, "weight"))
print(Dog.__dict__)

print(new_dog.test)