print("Let me find the square root of your number!")
x =input("Please input a positive number: ")
float_x = float(x)
count = 1
y = float_x/2

while pow(y, 2) >= (float_x + .01 or float_x - .01):
    print("Iteration: {}.".format(count))
    print (y)
    count += 1
    y = (y + (float_x/y))/2 #Newton's method y'all!

print("The square root of {} is {}".format(x, y) )
