#intentos 8 
#elegir un nombre y un numero 
from random import randint
intentos=0 
nombre=input("cual es tu nombre? ")
 
numeroramdom=randint(1,100)


while intentos < 8:
    numerousuario= int(input("escribe aca el numero: "))
    intentos+=1
    if numerousuario==numeroramdom:
        print("estas correcto")
    if numerousuario!=numeroramdom:
        print("numero incorrecto")
        


if numerousuario != numeroramdom:
    print(f"tu intentos se agotaron tu numero random era { numeroramdom}")

