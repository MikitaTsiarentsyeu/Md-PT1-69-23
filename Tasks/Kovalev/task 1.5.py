#Welcome to Number Randomizer
import random 
right = input("Please enter the right limit of number\n")
right = int(right)
left = input("Please enter the left limit of number\n")
left = int(left)
print("Your random number is")
print(random.randrange(right, left))
print("Good Luck, Have Fun!")






