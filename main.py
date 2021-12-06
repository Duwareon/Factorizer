#!/usr/bin/env Python3
from sympy import *
from sys import argv
init_printing(use_unicode=False)

# Setup the input polynomial
try:
	polynomstr = argv[1]
except:
	polynomstr = "9*x**2-18*y"
polynomial = parse_expr(polynomstr, {'x':Symbol('x', real=True), 'y':Symbol('y', real=True)}) 



def nfactor(polynomial):
	separateterms = Add.make_args(polynomial)
	numofterms = len(separateterms)
	denom = gcd(separateterms)
	
	# If the gcd isn't 1, factor the expression. I'm using factor() here because if I multiply it, it'll display wrong sometimes.
	# I do have the correct math done, it just tries to make the equation look nice if I multiply it like normal and it makes it not factored anymore.
	# It's either this or having it display certain things as 3*(4/3)
	if denom != 1:
		return (factor(denom * (polynomial / denom)))
	
	# Check if the polynomial is a binomial
	elif numofterms == 2:
			
		# Check if the second term is a monomial or not
		# The check happens because it's easier to check if it's negative when we know if it's a normal number
		isNomial = True
		try:
			Poly(separateterms[1])
		except:
			isNomial = False
		
		if isNomial:
			def isPos(val):
				return not (any(ele < 0 for ele in Poly(val).all_coeffs()))
		
		else:
			def isPos(val):
				return val<0
		
		# Check if the binomial is square
		# If not, then check for cubes
		if isperfectroot(polynomial, 2):
			#print("Square")
			# Check if the second term is negative 
			if isPos(separateterms[1]):
				return squarediff(polynomial)
						
			else:
				return False
				
		elif isperfectroot(polynomial, 3):
			#print("Cube")
			a = cbrt(abs(separateterms[0]))
			b = cbrt(abs(separateterms[1]))
			
			if (isPos(separateterms[1])):
				return (a+b)*(a**2-a*b+b**2)
			
			else:
				return (a-b)*(a**2+a*b+b**2)
		
		else:
			return False
			
	elif numofterms == 3:
		pass
	
	return True

# NOTE: this doesn't work properly because of the fact that sympy doesn't work properly with rooted exponents
def isperfectroot(binomial, num):
	args = Add.make_args(binomial)
	squaretest = []
	
	for i in range(0, 1):
		if floor(root(abs(args[i]), num)+0.5)**num == args[i]:
			squaretest.append(True)
		else: squaretest.append(False)
	
	return False in squaretest

# a**2 - b**2 = (a+b)(a-b)
def squarediff(polynomial):
	args = Add.make_args(polynomial)
	
	# TODO: make this not display as sqrt(x**2)
	# It's hard to do because for some reason simplify() doesn't make that change
	a = sqrt(abs(args[1]))
	b = sqrt(abs(args[0]))
	
	return (a+b)*(a-b)

print("My program:")
pprint(nfactor(polynomial))
print("Expected answer:")
pprint(factor(polynomial))
