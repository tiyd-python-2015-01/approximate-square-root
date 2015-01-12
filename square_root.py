response = int(input("Enter a positive number:"))
guess = response - .01

while True:
    x = (guess + (response/guess))/2
    if (guess - x < .01):
        break
    guess -= .01

print("The square root of {} is {}".format(response, guess))
