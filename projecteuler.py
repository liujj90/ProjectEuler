
'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
def sumMult3and5(upperbound):
	value  = 0
	for i in range (1, upperbound):
		if i % 3 == 0 and i % 5 != 0:
			value += i
		elif (i % 5 == 0):
			value += i
	return value


'''
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def evenfibb(upperbound):
	fibb = [1,1]
	position = len(fibb) -1
	summed = 0
	value = 0
	while value < upperbound:
		value = fibb[position] + fibb[position - 1]
		fibb.append(value)
		position += 1
	for item in fibb:
		if item %2 ==0:
			summed += item
	return summed

'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def isprime(x):
	# make sure number is a positive integer
	x = abs(int(x))
	# cant be 0 or 1
	if x  < 2:
		return False
	# two is a prime
	elif x == 2:
		return True
	# even numbers other than two are not primes
	elif x %2 ==0:
		return False
	#check every odd number until sqrt of x as larger numbers will need to be multiplied by smaller number (already checked)  
	for i in range(3, int(x**0.5)+1, 2):
		if x % i  == 0:
			return False
	return True

def largestPrimefactor(x):
	factors = []
	# largest factor would be sqrt of number
	for i in range(1, int(x**.5)+1):
		if x % i == 0:
			factors.append(i)
	# number may be a prime too
	factors.append(x)
	primes  = []
	# check if prime, return largest (last)
	for factor in factors:
		if isprime(factor) == True:
			primes.append(factor)
	return primes[-1]

'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(x):
	#convert to string
	x = str(x)
	# if odd number of digits, false
	if len(x) %2 !=0:
		return False
	else:
		for n in range(len(x)/2):
			if x[n] != x[-(n+1)]:
				return False
		else:
			return True


for x in range(900,1000):
	for y in range(900,1000):
		if isPalindrome(x*y) == True:
			print ('%d * %d = %d - palindrome' %(x,y,x*y))

'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time

def checkDivs(num, maximum):
	for i in range(maximum/2 ,maximum + 1):
		if num % i == 0:
			continue
		else:
			return False
	return True


def smallestMultiple(maximum):
	start = time.time()
	num = maximum
	while not checkDivs(num, maximum):
		num += maximum
	end = time.time()
	print (num, end - start)

'''
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np
#import time

def SumSquareDiff(maximum):
	start = time.time()
	x = np.array(range(1, maximum+1))
	sumofsq = sum(x**2)
	sqofsum = sum(x)**2
	end =  time.time()
	return (sqofsum - sumofsq, end - start)

'''
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# use isprime function from problem 3

# find 10001st prime
def findprime(target):
	primes = []
	x = 1
	while len(primes) < target:
		if isprime(x) == True:
			primes.append(x)
		x+=1
	#get last prime		
	return primes[-1]


'''
Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''
# store as multi-line string
seq = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''
# convert to list
sequ = [int(x) for x in seq if x != '\n']

def multiplyListItems(x):
	mult = 1
	for item in x:
		mult *= item 
	return mult

def multiplyLargestStr(sequence, length):
	largestseq = sequence[0:length]
	start = 1
	for i in range(len(sequence)-(length-1)):
		end = start + length
		newseq = sequence[start:end]
		if multiplyListItems(newseq) > multiplyListItems(largestseq):
			largestseq = newseq
		start += 1
	return (largestseq, multiplyListItems(largestseq))

'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def pythagoras(a,b):
	return (a**2 +b**2)**.5

def findPythaTriplet(summed):
	for a in range(1, summed):
		for b in range(1, summed):
			c = pythagoras(a,b)
			if summed== a+b+c:
				return a*b*c


'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# use isprime function 

def sumprimes(limit):
	x = 0
	for i in range(1,limit):
		if isprime(i)== True:
			x += i
	return x

'''
problem 11
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''
sequence = '''

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
seq = [x.split(' ') for x in sequence.splitlines()]
seq = [[int(x) for x in y] for y in seq]

def adjProducts():
	max_prod = 0
	for i in range(len(seq)):
		for j in range(len(seq) - 4):
	        # right/left products
			prod = seq[i][j]*seq[i][j+1]*seq[i][j+2]*seq[i][j+3]
			if prod > max_prod: 
				max_prod = prod
	        # up/down products
	for i in range(len(seq)-4):
		for j in range(len(seq)):       
			prod = seq[i][j]*seq[i+1][j]*seq[i+2][j]*seq[i+3][j]
	    	if prod > max_prod: 
	    		max_prod = prod
	 
	# diagonal products
	for i in range(len(seq)-4):
		for j in range(len(seq)-4):
			prod = seq[i][j]*seq[i+1][j+1]*seq[i+2][j+2]*seq[i+3][j+3]
			if prod > max_prod: 
				max_prod = prod
	for i in range(3,len(seq)):
		for j in range(len(seq)-4):
			prod = seq[i][j]*seq[i-1][j+1]*seq[i-2][j+2]*seq[i-3][j+3]
			if prod > max_prod: 
				max_prod = prod
	return (max_prod)