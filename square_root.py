guess_number = 1
error = 0.01
iteration = 1


try:
    user_input = input("Please enter a positive number you "
                       "would like to find the square root of: ")

    squared_number = float(user_input)

    if squared_number >= 0:

        squared_number = float(user_input)
        while not guess_number**2 - error < squared_number < guess_number**2 + error:
            print("This is iteration", iteration)
            iteration += 1
            print("The number used to guess was", guess_number)
            guess_number = (guess_number + (squared_number/guess_number))/2

        print("*"*60)
        print("Final Answer:", guess_number, "Last Iteration:", iteration)

    else:
        #complex_number = (complex(user_input))
        #while not guess_number**2 - error > complex_number > guess_number**2 + error:
            #print("This is iteration", iteration)
            #iteration += 1
            #print("The number used to guess was", guess_number)
            #complex_number = (guess_number - (complex_number/guess_number))/2
        #print("*"*60)
        #print("Final Answer:", guess_number, "Last Iteration:", iteration)
        print("Ooops, not an odd number!")


except ValueError:
    print("Oops! that wasn't a number, please try again.")
