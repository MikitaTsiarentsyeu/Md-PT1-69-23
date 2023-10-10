def calculate_power(number, degree):
    """ a recursive function to calculate the power of a given number """

    if degree == 0:
        return 1
    if degree < 0:
        return calculate_power(number, degree+1)/number
    if degree > 0:
        return number * calculate_power(number, degree-1)

input_number = input("Please, input a number: ")
input_degree = input("Ok, input a degree: ")

if input_number == '0' and input_degree == '-1':
    print('Infinity')
else:
    print(calculate_power(int(input_number), int(input_degree)))