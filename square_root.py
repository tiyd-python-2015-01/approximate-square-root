epsilon = 0.01

while True:

    user_input = input("Enter a positive number: ")

    try:
        number = float(user_input)
    except ValueError:
        print("Not a valid number.")
        continue
    if number<0:
        print("That's not a positive number.")
    else:
        break

# Initialize a guess. What makes a good guess? Something closer than n-1, like n/2.
guess = number/2
# While loop until a guess variable is good enough.
loop_pass = 1
while (abs(pow(guess,2)-number)> epsilon):
    guess = (guess + (number/guess))/2
    print("Pass number {}: {}".format(loop_pass, guess))
    loop_pass += 1

print("The square root of {} is {}".format(number, guess))
