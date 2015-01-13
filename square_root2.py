user_input = int(input("Enter a positive number: "))

guess = 1
count = 1

while guess != user_input:
    guess = (guess + user_input/guess)/2
    count += 1
    print("Guess #{}: {}".format(count, guess))

    if count == 6:
        print("The square root of {} is {}.".format(user_input, guess))
        break

    else:
        continue
