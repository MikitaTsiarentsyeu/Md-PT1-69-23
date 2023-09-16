class BaseClass:

    test = "test"

class Animal(BaseClass):

    name = "test animal"

    def say_something(self):
        print(f"hello, my name is {self.name}")


class Dog(Animal):

    def say_something(self):
        print("woof!")


d = Dog()
print(d.name)
d.say_something()

print(Animal.__dict__)
print(Dog.__dict__)
print(d.__dict__)

print(Dog.__mro__)
print(Animal.__mro__)
print(BaseClass.__mro__)
print(object.__mro__)


class A:

    def test(self):
        print("test A")

class B:

    def test(self):
        print("test B")

class C(B, A):

    def test(self):
        print("test C")


class D:

    def test(self):
        print("test D")

class E:

    def test(self):
        print("test E")

class F(D, E):

    def test(self):
        print("test F")

class G(C, F):

    def test(self):
        print("test G")


print(G.__mro__)



class Dog:

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

class GuardDog(Dog):

    def __init__(self, name, color, woof_sound) -> None:
        super().__init__(name, color)
        Dog.__init__(self, name, color)
        self.woof_sound = woof_sound