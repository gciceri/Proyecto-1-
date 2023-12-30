#primero preguntar el nomrbe al usuario
#tirar un random un numero desde el 1 al 100
# el usuario tiene 8 intentos para achuntar
# pueden haber 4 respuestas: le achuntaste, el numero esta mas arriba
# el numero esta mas abao, o ese numero no esta permitido 
# si le achunta le dice felicitaciones y le dice cuantas veces intento

usuario=input("cual es tu nombre:")
from random import *
numero=randint(1,100)
print(numero)
numero_usuario=input("elie un numero:")
if numero==numero_usuario:
    print("tu numero es correcto")
if numero>numero_usuario:
    print("el numero esta mas arriba")
if numero<numero_usuario:
    print("tu numero esta mas abao")
if numero >100  :
    print("estas fuera del rango")       # esta algo mal     