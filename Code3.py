import sympy
from sympy import symbols
from sympy import solve
x= symbols('x')
eq= input('Enter equation: 0 = ')
solution= solve(eq,x)
for s in solution:
    print("x= ", s)
#ex. Enter equation 0 = (x-1)*(x+2)
