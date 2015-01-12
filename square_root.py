import sys


def find_square_root(number):
    guess = number * .9
    guess_count = 0

    while guess**2 - number > 0.01 or guess**2 - number < -0.01:
        guess = (guess + number/guess)/2
        guess_count += 1
        print("The current guess is: {}"
              " guess number: {}".format(guess, guess_count))
    return guess

try:
    user_input = float(input("Please enter a number: "))
except ValueError:
    print("Please enter a valid number greater than zero!")
    sys.exit()

if user_input < 0:
    answer = complex(0, find_square_root(user_input * -1))
else:
    answer = find_square_root(user_input)

print("The answer is: {}".format(answer))
