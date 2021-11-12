#!/usr/bin/env Python3
from sympy import *
init_printing(use_unicode=True)

#x, y = symbols('x y')

#polynomstr = "9*x**2-49"
polynomstr = "9*x**2-25*y**2"

polynomial = parse_expr(polynomstr, evaluate=False)



def nfactor(polynomial):
    # set up some useful variables.
    separateterms = Add.make_args(polynomial)
    numofterms = len(separateterms)
    denom = gcd(separateterms)
    #pprint(denom)
    

    # If the gcd isn't 1, factor the expression. I'm using factor() here because if I multiply it, it'll display wrong sometimes.
    # I do have the correct math done, it just tries to make the equation look nice if I multiply it like normal and it makes it not factored anymore.
    # It's either this or having it display certain things as 3*(4/3)
    if denom != 1:
        return (factor(denom * (polynomial / denom)))

    # Check if the polynomial is a binomial
    elif numofterms == 2:
        # Check if the binomial is able to be square rooted
        if perfectsquare(polynomial):
            
            # Check if the second term is a monomial or not
            # The check happens because it's easier to check if the second term is negative this way
            isNomial = True
            try:
                Poly(separateterms[1])
            except:
                isNomial = False
            
            
            if isNomial:
                # Check if the second term is negative
                if any(ele < 0 for ele in Poly(separateterms[-1]).all_coeffs()):
                    return squarediff(polynomial)
                
                else: return False
                
            else:
                if (separateterms[1]/-1)>0:
                    return squarediff(polynomial)
                else: return False
        else:
            pass
    
    elif numofterms == 3:
        pass

    elif numofterms == 4:
        pass
    
    return False
    

def perfectsquare(polynomial):
    args = Add.make_args(polynomial)
    return True
    
def squarediff(polynomial):
    #a**2 + b**2 = (a+b)(a-b)
    args = Add.make_args(polynomial)

    # TODO: make this not display as sqrt(x**2)
    a = (sqrt(args[0]))
    b = sqrt(abs(args[1]))

    return ((a+b)*(a-b))

pprint(nfactor(polynomial))
pprint(factor(polynomial))
pprint(sqrt(6**2) == 6) 
