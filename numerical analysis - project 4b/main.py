"""
Group: Daniel Houri , 209445071
       Eve Hackmon , 209295914
       Yakov Shtefan , 208060111
       Vladislav Rabinovich , 323602383
       Aaron Hajaj , 311338198
       Git: https://github.com/EveHackmon/Numerical_Analysis.git
"""
import math
import sympy as sp

def trapezoidal_rule(f, a, b, n):
    f1 = sp.lambdify(x, f)
    h = (b - a) / n
    T = f1(a) + f1(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f1(x_i)

    integral *= h

    Ftags = sp.lambdify(x , sp.diff(sp.diff(f)))
    error = abs((((b-a)*3)/(12*n*2)) * Ftags(1))
    return integral , error

if __name__ == '__main__':
    x = sp.symbols('x')
    f = sp.sin(x)
    result = trapezoidal_rule(f, 0, math.pi, 4)
    print("Approximate integral:", result[0] , "\nError:" , result[1])