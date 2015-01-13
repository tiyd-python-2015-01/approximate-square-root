y = int(input("Enter a postive number:"))
x = y - 0.01

while True:
    i = (x + (y/x))/2
    if(x - i) < .01:
        break
    x -= .01
print("The Square Root of {} is {}".format(y, x))
