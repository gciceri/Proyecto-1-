import random 
print(random.randint(1,2))

#Funciones
print("Funciones\n")

def elevado(a,b):
    return a*b

print(elevado(2,2),"\n\n")

def cuadrado(x):
    return x**2
sq2=cuadrado(9)
print(sq2)

print("\n ARGUMENTO OPCIONALES")

def distancia(x1,y1,x0=0, y0=0):
    return((x1-x0)**2 + (y1-y0)**2)**(1/2)
print(distancia(1,2))

print("\nLibreria")
# librerias
# Tres maneras para importar librerias en Python

# import libreria
# from libreria import modulo
# import librerias as lib

import math
print(math.sqrt(16)) #=4
print(math.pi)
print(math.pow(2,3))# 2 elevado a 3 
print(math.exp(1))

#Eercicios 
print("\n\nEERCICIO B&S")

from scipy.stats import norm

s=60
k=65
T=0.25
r=0.08
sigma=0.3


N=norm.cdf
r=0.08
def opcion(s,k,T,sigma,kind="call"):
    d1=(math.log(s/k)+T*((r+sigma**2)/2))/(sigma*T**0.5)
    d2=d1-sigma*T**0.5
    return s*N(d1)-k*math.exp(-r*T)*N(d2)
print(opcion(60,65,0.25,0.3,"call"),"\n\n")
resultado_call=opcion(60,65,0.25,0.3,"call")
#eercicio 2 
print("Paridad Put Call")

def paridad(s,k,T):
    return resultado_call-s+k*math.exp(-r*T)
print(paridad(60,65,0.25))


def hello(to="alguien"):
    print(f"(hello,{to})")

name=input("whats your name")
hello(name)    

def main():
    x=int(input("escribe el numero "))
    print(f"el cuadrado de {x} es",square(x) )

def square(n):
    return n**2

main()

