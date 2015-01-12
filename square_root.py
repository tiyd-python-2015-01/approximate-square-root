#Newton's method of successive approximations says that whenever we have a
#guess y for the value of the square root of a number x, we can get a
#better guess (one closer to the actual square root) by averaging y with x/y. If we do this over and over, we should be able to get a very accurate guess.

#You have to write a script that asks the user for a positive number and
#then compute the square root with a maximum error of 0.1.
#You then print out your answer to the user.



x = int(input ("Give me a positive number: "))
y = 0.1

while y < (x / 2):
    if (y ** 2) <= (x - .01):
        y += 0.1
    else:
        break

print("The square root of {} is {}.".format(x, round(y, 3)))
