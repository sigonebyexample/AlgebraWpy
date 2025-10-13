import sympy
from sympy import symbols
from sympy.solvers import solve
x = symbols('x')
eq = input("Enter your equation (in terms of x): ")
solve(eq,x)
print("x= ", solve(eq,x))
