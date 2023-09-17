class Animal:

    def say_something(self):
        print("something")

class Dog(Animal):

    def say_something(self):
        print("booork!")

class Cat(Animal):

    def say_something(self):
        print("Nya!")

class Human:

    def say_something(self):
        print("Hello, my name is Anatoly")

def test_saying(animals):
    for animal in animals:
        animal.say_something()

test_saying([Animal(), Dog(), Cat(), Human()])

5+5
'5'+'10'
# 5+'5'

print(int.__add__(5, 5))
print(str.__add__('5', '5'))

print('5'.__add__('10'))