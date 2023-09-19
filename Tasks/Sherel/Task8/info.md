> **Note**
>by @szerel

# Home Work Task 8 by Sherel
![python-version](https://img.shields.io/badge/python-3.11-blue.svg)

## About
Here is a program that has 2 modules (but for greater visualization and code layout, it uses an additional tabulate module), one is console, the other is server.

The program allows the user to view, store and search the database for information about works of art by great artists. (database stored on hard drive)

The console module allows the user to perform actions:
- Add to collection
- Show all available collection
- Find in the collection by the desired key - the desired option
- End of the program

The search is implemented through a generator function that is reused for each individual key, namely title, author, year, genre.
```
def gen_search_in_collection(self, search_input, by):
    data = DataBase.get_collection(self)
    for i in data:
        if search_input in i[by]:
            yield i
```

## Screenshots
### The console module
![menu](https://telegra.ph/file/5e951051375cf7e5bf1b8.png)
### Add to collection
![task1](https://telegra.ph/file/23a2389bf55e73f60a8e9.png)
### Show all available collection
![task2](https://telegra.ph/file/8621a366c517e7734bce0.png)
### Find in the collection
![task3](https://telegra.ph/file/ae230c7752780735240fa.png)


## Prerequisites
- Python 3.9+

1. Install the dependencies using `tabulate` module:

I use this module only for visual enjoyment when displaying my collections in the user console
```shell
pip install tabulate
```


## Disclaimer
This code, is riddled with humor and satire. Please don't take it too seriously or take it personally. After all, programming is an art that allows us to express ourselves, even if it's in a funny and ironic way. Use code with a smile on your face, and remember that true programming prowess also includes the ability to handle the nuances of life with ease and good humor. Happy coding!