from random import *

intentos = 0 # este lo pongo porque parte del 0 el loop 
numero_secreto=randint(1,100)
nombre_usuario=input("escribe tu nombre:")

print(f"Bueno {nombre_usuario}, escribe elige un numero entre el 1 al 100, tienes 8 intentos")

while intentos < 8 : 
    estimado= int(input("escribe el numero:" ))
    intentos+=1 #este lo tengo que poner para que se repita el loop y avance uno 

    if numero_secreto==estimado:
        print("tu numero es correcto")
    if numero_secreto>estimado:
        print("el numero esta mas arriba")
    if numero_secreto<estimado:
        print("tu numero esta mas abao")
    if numero_secreto >100  :
        print("estas fuera del rango")
        break 
if estimado != numero_secreto:
    print(f"lo siento has agotado los intentos, el numero era: {numero_secreto} ") 
       