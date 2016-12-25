'''
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. '''


# long division function

def longdiv(denom):
    numerator = 1
    remain = []
    remainder = (numerator % denom) * 10
    while remainder not in remain:
        remain.append(remainder)
        remainder = (remainder % denom) *10
    return len(remain)
answer = 0
currlen = 0
for i in range(1, 1000):
    currans = longdiv(i)
    if currans > currlen:
        answer = i
        currlen = currans
        



guess = [50]
toohigh = [100]
toolow = [0]
while True:
    print ('Is your secret number %d?' %guess[-1])
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if user == 'h':
        toohigh.append(guess)
        newguess = int((max(toolow)+ min(toohigh))/2)
        guess.append(newguess)
    elif user == 'l':
        toolow.append(guess)
        newguess = int((max(toolow)+ min(toohigh))/2)
        guess.append(newguess)
    elif user == 'c':
        print ('Game over. Your secret number was:', guess[-1])
        break
    else:
        print ('Sorry, I did not understand your input.')
        print ('Is your secret number %d?' %guess[-1])
        user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
