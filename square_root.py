squared_number = float(input("Please enter a positive number you "
                             "would like to find the square root of: "))
guess_number = 0.01
iteration = 1


while not (guess_number**2 - 0.0001) < squared_number < (guess_number**2 + 0.00001):
    print("This is iteration {}".format(iteration))
    iteration += 1
    print("The number used to guess was", guess_number)
    average_number = (guess_number + (squared_number/guess_number))/2
    guess_number = average_number
print("Final Answer:", guess_number)
