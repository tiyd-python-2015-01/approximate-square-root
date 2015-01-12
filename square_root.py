while True:
    try:
        response = int(input("Give a positive number please. "))
        break
    except:
        print("You didn't put in a number!")

if response <= 0:
    print("You didn't give a positive number!")

guess = response - .01
it = 0

while True:
    it += 1
    print("This is the iteration: {}. This is the guess:{}.".format(it, guess))
    x = (guess + (response/guess)) / 2
    if (guess - x < .01):
        break
    guess -= .01

print(guess)
