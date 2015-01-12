from random import randint

while True:
    try:
        num = int(input("Enter a Positive Number: "))
        if num >0:
            break
        else: 
            print("Oops!  That number is not positive.  Try again...")
    except ValueError: 
        print("Oops!  That was not a number.  Try again...")

x0=randint(1,num)
i=1
while True:
   print("This is iteration ",i,"and my current guess is", x0)
   x1=(x0+(num/x0))/2
   if (abs(x0-x1) < 0.01):
        break
   x0=x1
   i+=1
print("The square root of",num,"is",x0)
