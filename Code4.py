from sympy import *
var('x y')
first= 2*x + 10
eq1= Eq(first,y)
sol= solve(eq1,x)
print("x= ", sol[0])
