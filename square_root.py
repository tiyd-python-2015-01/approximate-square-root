#Jason Aylward
#Homework 1:

def square(original):
    guess = 0.1
    iteration = 1
    while not abs((guess * guess) - original) < 0.0001 :
        guess = (guess + original/guess) / 2
        print("{}: {}".format(iteration,guess))
        iteration += 1
    return guess

while True:
    try:
        original_number = int(input("Enter a positive number: "))
        break
    except:
        print("Try to stick with Positive Integers.")
final_root = square(original_number)
print("The square root of {} is {}".format(original_number, final_root))
