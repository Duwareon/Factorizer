#!/usr/bin/env Python3
from sympy import *
init_printing(use_unicode=True)

#x, y = symbols('x y')

#polynomstr = "9*x**2-49"#*x"
polynomstr = "6*(x**2) + 6*(x+1)"

polynomial = parse_expr(polynomstr, evaluate=False)



def nfactor(polynomial):
    # Check for the greatest common denominator.
    separateterms = Add.make_args(polynomial)
    numofterms = len(separateterms)
    #return numofterms, separateterms
    denom = gcd(separateterms)
    #squarediff = checksquarediff(polynomial)
    #pprint(separateterms)

    # If the gcd isn't 1, factor the expression. I'm using factor() here because if I multiply it, it'll display wrong sometimes.
    # I do have the correct math done, it just tries to make the equation look nice if I multiply it like normal and it makes it not factored anymore.
    if denom != 1:
        return (factor(denom * (polynomial / denom)))

    """
    elif numofterms == 2 & (separateterms[-1]/-1)<0:
        print("pog")
        return sqaurediff(polynomial)
    
    elif numofterms == 3:
        pass

    elif numofterms == 4:
        pass
    """

    else:
        return None
    #return simplify(sqrt(polynomial/6)) 

def sqaurediff(polynomial):
    #a**2 + b**2 = (a+b)(a-b)
    args = Add.make_args(polynomial)
    #polynomial = Poly(polynomial)
    return Poly(args[0]), Poly(LT(args[0])).all_coeffs()
    #return Pow(sqrt(args[0].coeff(x, 2)), 2, evaluate=False)

pprint(nfactor(polynomial))


