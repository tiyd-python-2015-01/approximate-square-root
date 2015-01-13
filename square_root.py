number = int(input("Give me a positive number and I shall give you the square\n>:"))
new_guess = number

while True:
    print ("Testing: {}".format(new_guess))
    last_guess = new_guess
    new_guess = (new_guess + number/new_guess) / 2
    if abs(new_guess-last_guess) < .01:
        break
    else:
        new_guess -= .01





print("The square root of {} is {}!".format(number,new_guess))
