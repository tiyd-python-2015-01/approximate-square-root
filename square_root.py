epsilon = 0.01

user_input = input("Enter a positive number: ")

try:
    number = float(user_input)
except ValueError:
    print("Not a valid number.")
# Initialize a guess. What makes a good guess? Something closer than n-1, like n/2.
guess = number/2
# While loop until a guess variable is good enough.
while (abs(pow(guess,2)-number)> epsilon):
    guess = (guess + (number/guess))/2

print("The square root of {} is {}".format(number, guess))
