
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