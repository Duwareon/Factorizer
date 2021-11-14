#!/usr/bin/env Python3
from sympy import *
from sys import argv
init_printing(use_unicode=True)

# Setup the input polynomial
polynomstr = argv[1]
polynomial = parse_expr(polynomstr, evaluate=False)


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
    if numofterms == 2:
        
        # Check if the binomial is square
        # If not, then check for cubes
        if perfectsquare(polynomial, 2):
            
            # Check if the second term is a monomial or not
            # The check happens because it's easier to check if it's negative when we know if it's a normal number
            isNomial = True
            try:
                Poly(separateterms[1])
            except:
                isNomial = False
            
            
            if isNomial:
                # Check if the second term is negative 
                if any(ele < 0 for ele in Poly(separateterms[-1]).all_coeffs()):
                    return squarediff(polynomial)
                
                else:
                    print("Not A**2-B**2")
                    return False
                
            
            else: 
                # Check if the second term is negative
                if separateterms[1]<0:
                    return squarediff(polynomial)
                else:
                    print("Not A**2-B**2")
                    return False
        elif perfectsquare(polynomial, 3):
            # TODO: add cube difference/sum methods of factoring
            return True 
            
           
    elif numofterms == 3:
        pass
    
    elif numofterms == 4:
        pass
 
    return False

def perfectsquare(binomial, num):
    args = Add.make_args(binomial)
    squaretest = []

    if num == 2:
        def test(arg):
            return floor(sqrt(arg)+0.5)**2
    elif num == 3:
        def test(arg):
            return floor(cbrt(arg)+0.5)**3
    
    for i in range(0, 1):
        if test(args[i]):
            squaretest.append(True)
        else: squaretest.append(False)
    return False in squaretest

# a**2 + b**2 = (a+b)(a-b)
def squarediff(polynomial):
    args = Add.make_args(polynomial)
    
    # TODO: make this not display as sqrt(x**2)
    # It's hard to do because for some reason simplify() doesn't make that change
    a = sqrt(args[0])
    b = sqrt(abs(args[1]))
    
    return (a+b)*(a-b)

pprint(nfactor(polynomial))
pprint(factor(polynomial)) 
