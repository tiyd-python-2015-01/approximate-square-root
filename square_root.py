squared_number = float(input("Please enter a positive number you "
                             "would like to find the square root of: "))
guess_number = 1
error = 0.0001
iteration = 1


while not guess_number**2 - error < squared_number < guess_number**2 + error:
    print("This is iteration", iteration)
    iteration += 1
    print("The number used to guess was", guess_number)
    average_number = (guess_number + (squared_number/guess_number))/2
    guess_number = average_number
print("Final Answer:", guess_number)
