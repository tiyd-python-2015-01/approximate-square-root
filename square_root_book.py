x = float(input("Enter a positve number: "))
epsilon = .01
ans = 0.0
guesses = 0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += 0.01
    guesses += 1
    ##print (ans)
if abs(ans**2 - x) >= epsilon:
    print ('Failed on square root of', x)
else:
    print (ans, 'is close to square root of', x)
    print ("It took", guesses)
