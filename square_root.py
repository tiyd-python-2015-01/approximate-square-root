def square_root(user_input):

    if user_input == 1:
        return 1
    elif user_input < 0:
        return complex(0, newtons_formula(user_input * -1))
    else:
        return newtons_formula(user_input)

def newtons_formula(target):
    next_guess = target * .9
    epsilon = 0.01
    count = 1

    while (next_guess ** 2 - target) > epsilon:
        next_guess = (next_guess + (target / next_guess)) / 2
        print("Iteration: {}".format(count))
        print("Current Guess: {}\n".format(next_guess))
        count += 1

    return next_guess

while True:
    try:
        user_input = float(input("Enter number: "))
        break
    except ValueError:
        print("Not a Number!")

print("The square root is approximately {}".format(square_root(user_input)))
