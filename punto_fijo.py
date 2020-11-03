#Implementación del método del punto fijo

from math import *
import sympy as sp 
from scipy.misc import derivative





#Prueba derivada - salida simbolica
def derivada():
    x = sp.Symbol('x')
    y = (e**x + 5*x)**(1/2)
    return sp.diff(y,x)

print(derivada())

#Prueba derivada y evaluacion numerica
f = lambda x: derivada()
print(derivative(f,0, dx=1e-8))

#Funcion prueba despejada
def pol_prima(x): 
    return (2*x +1)**(1/3)
    
def puntofijo(f, p0, tol, n): #Método del punto fijo
    i = 1
    while i <= n:
        p = f(p0)
        print("Iter= ", "%03d" % i, "; p =", "%.14f" % p)
        if abs(p-p0) < tol:
            print("Error final:"," %.6f" % abs(p-p0))
            return p
        p0 = p
        i +=1
    print("Iteraciones agotadas:Error!")
    return 

#pol(x), po = 0.9, tol = 10^-10, n=100

print("Pol prueba")
puntofijo(pol_prima, 0, 0.00001, 12)
