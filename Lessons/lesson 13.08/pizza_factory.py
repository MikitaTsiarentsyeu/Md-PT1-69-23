def prepare(name):
    print(f"starting a new {name} pizzamaking process")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding some {ingridient}")

def grind_cheese():
    print("griding cheese")

def bake(temp, time):
    print(f"baking at {temp} for a {time} minutes")

def done():
    print("boxing")
    print("slicing")
    print("done!")

# def make_peperroni():
#     prepare("peperroni")
#     add_ingridient("peperroni")
#     grind_cheese()
#     bake(150, 5)
#     done()

# def make_double_peperroni():
#     prepare("peperroni")
#     add_ingridient("peperroni")
#     add_ingridient("peperroni")
#     grind_cheese()
#     bake(150, 5)
#     done()

# def make_margarita():
#     prepare("margarita")
#     add_ingridient("tomatoes")
#     add_ingridient("basilik")
#     grind_cheese()
#     bake(150, 3)
#     done()

def pizza_factory(name, ingridients, temp, time):
    def factory_method():
        prepare(name)
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake(temp, time)
        done()
    return factory_method


make_peperroni = pizza_factory("peperroni", ["peperroni"], 150,  5)
make_double_peperroni = pizza_factory("peperroni", ["peperroni"]*2, 150,  5)
make_margarita = pizza_factory("margarita", ["tomatoes", "basilik"], 150, 3)

make_double_peperroni()