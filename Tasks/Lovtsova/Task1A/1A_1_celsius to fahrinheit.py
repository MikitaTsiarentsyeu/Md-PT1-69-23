#1.Write a program that converts Celsius to Fahrenheit

celsius=input('Enter the Celsius:\n')
try:
    celsius=float(celsius)
    if celsius>=(-273):
        fahrenheit=round((celsius*1.8+32), 2)
        print(celsius, " Celsius is" , fahrenheit, "Fahrenheit")
    else:    
        print("This temperature is lower then the existion one!\n")

except ValueError:
    print ("It's not correct. Please, try again!\n")