import time


def separation():
    print("-"*30)
    time.sleep(3)


def greeting_message():
    print("welcome to digital anime series storage!")


def goodbye_message():
    print("Thank you for using our storage, have a great day!")


def action():  # todo
    print("""What would you like to do?

          1. """)
    return input()
