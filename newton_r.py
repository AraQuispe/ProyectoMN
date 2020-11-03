#Implementación del método de Newton

from math import *

#Ejemplo función
def expo(x):
    return x**2+exp(-2*x)-2*x*exp(-x)
#Ejemplo de derivada de función
def expoprima(x):
    return 2*x-2*exp(-2*x)-2*exp(-x)+2*x*exp(-x)

def newton(f, fprima, p0, tol, n):
    i = 1
    while i<=n:
        p = p0-f(p0)/fprima(p0)
        print(" I ter = " , " %03d " % i, " ; p = " , " %.14f " % p)
        if abs(p-p0) < tol:
            return p
        p0 = p
        i += 1
    print(" Iteraciones agotadas: Error!")
    return

print(" \n" +r"-- Newton funcion expo(x):" +" \n")
newton(expo, expoprima, 4.0, 1e-8, 100)