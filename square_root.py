from random import randint

while True:
    try:
        value_read = int(input("Enter an Integer Number: "))
        if value_read > 0:
            imaginary=' '
            num=value_read
            break
        else: 
            imaginary='i'
            num=abs(value_read)
            break
    except ValueError: 
        print("Oops!  That was not an integer number.  Try again...")

x0 = randint(1,num)
i = 1
while True:
    print("This is iteration ",i,"and my current guess is", x0)
    x1 = (x0 + (num / x0))/2
    if (abs(x0-x1) < 0.01):
        break
    x0 = x1
    i += 1
print("The square root of",value_read,"is",round(x0,2),imaginary)
