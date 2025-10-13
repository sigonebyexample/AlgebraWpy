from sympy import * 
var('x y')
eq= 2*x + 10*y + 4
eq2= x**2-4
print(factor(eq))
print(factor(eq2))
