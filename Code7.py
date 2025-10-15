from sympy import *
var('x')
ex= 3* x - 12
equation= Eq(ex,0)
sol=solve(equation, x)
print("x= ", sol)