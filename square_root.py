y = int(input("Enter a positie Number "))
x = y - .01
guesses = 0

while True:
    i = (x + (y/x))/2
    if (x - i) < .01:
        break
    x -= .01
    guesses += 1
print ("The square root of {} is {}".format(y, x))
print ("It took ", guesses, "guesses")

##I worked with Micheal and Ben on this homework
