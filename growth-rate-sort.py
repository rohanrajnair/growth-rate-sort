
from sympy import *

def sort_funcs(funcs):
    has_swapped = True

    while(has_swapped == True):
        has_swapped = False
        for i in range(len(funcs) - 1):
            lim = limit(funcs[i]/funcs[i+1], x, oo)
            if lim == 0:
                funcs[i], funcs[i+1] = funcs[i+1], funcs[i]
                has_swapped = True


x = symbols('x')
my_funcs = [x**sqrt(log(x)), 7*x, 100*sqrt(x) + 2*x**0.25 + 100000, 2**(log(x)*log(x)), 2**(2*log(x)) + x**1.5, 3**x, ln(factorial(x)), 2**(1.5**x)]

sort_funcs(my_funcs)
print(my_funcs)


