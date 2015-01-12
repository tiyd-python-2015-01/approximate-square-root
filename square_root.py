response = int(input("Give a positive number please. "))

if response < 0:
    print("You didn't put in a positive number!")
    quit()

while True:
    try:
        break
    except:
        print("You didn't put in a number!")

guess = response / 2
it = 0

while True:
    it += 1
    print("This is the iteration: {}. This is the guess:{}.".format(it, guess))
    x = (guess + (response/guess)) / 2
    if (guess - x < .0001):
        break
    guess -= .25

print(guess)
