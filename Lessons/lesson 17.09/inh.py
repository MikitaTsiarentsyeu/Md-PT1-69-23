from abc import ABC, abstractmethod

class Dog(ABC):

    @abstractmethod
    def woof(self):pass


class GuardDog(Dog):

    def guard(self):
        print("I'll bite you!")

    def woof(self):
        super().woof()

class PoliteGuardDog(GuardDog):

    def guard(self):
        print("Could you please walk away?")

d = GuardDog()
d.woof()


class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

class Animal(ABC):

    @abstractmethod
    def eat(self, something):
        print(f"eating {something.name}")

    @abstractmethod
    def phe(self):
        print("phe...")

class Nevervore(Animal):

    def eat(self, something):
        super().phe()

    def phe(self):
        super().phe()

class Herbivore(Animal):

    standalone = True

    def eat(self, something):
        if something.type == "herbal":
            Animal.eat(self, something)
            return True
        else:
            if self.standalone:
                super().phe()
            return False
    
    def phe(self):
        super().phe()

class Carnivore(Animal):

    standalone = True

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
            return True
        else:
            if self.standalone:
                super().phe()
            return False

    def phe(self):
        super().phe()

class Omnivore(Carnivore, Herbivore):

    standalone = False

    def __init__(self) -> None:
        self.__chain = [Carnivore(), Omnivore()]

    def eat(self, something):
        for eater in self.__chain:
            if eater.eat(self, something):
                break
        else:
            super.phe()

        # if not Carnivore.eat(self, something):
        #     if not Herbivore.eat(self, something):
        #         super().phe() 

chicken = Food("chicken", 'meat')
grass = Food("grass", 'herbal')

c = Carnivore()
h = Herbivore()
o = Omnivore()

print(Omnivore.__mro__)

for food in [chicken, grass]:
    o.eat(food)