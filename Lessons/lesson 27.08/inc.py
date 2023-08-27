class Dog:

    __woof_sound = "Woof!"

    def __init__(self, name, breed, color=None):
        self.name = name
        self.__breed = breed
        if breed == "wss":
            self.__color = "white"
        else:
            self.__color = color
        self.__colored = False
        self.__initial_color = ""
        
    def set_name(self, new_name):
        self.__name = new_name.lower()

    def get_name(self):
        return self.__name


    def set_color(self, new_color):
        if not self.__initial_color:
            self.__initial_color = self.__color
        self.__color = new_color
        self.__colored = True

    def reset_color(self):
        self.__color = self.__initial_color
        self.__colored = False

    def get_color(self):
        return self.__color

    def get_breed(self):
        return self.__breed
    
    def woof(self):
        print(self.__woof)

    color = property(get_color, set_color)
    breed = property(get_breed)
    name = property(get_name, set_name)
    

zefirka = Dog("Zefirka", "wss")

zefirka.name = "Crocodile"
# zefirka.color = "black"
# zefirka.colored = True
# zefirka.set_color("black")
zefirka.color = "black"

# zefirka.__color = "white"


# print(zefirka.get_color())
print(zefirka.color)

print(zefirka.__dict__)
print(zefirka.breed)
zefirka.breed = "test"