from random import *
#Funciones
print("Funciones\n")

def elevado(a,b):
    return a*b

print(elevado(2,2),"\n\n")

x=12
print(f"elige un numero del uno al {x}")
target=randint(1,x)
while True:
    input_num=int(input("numero: "))
    if input_num==target:
        print("Le achuntaste")
        break
    elif input_num>target:
        print("el numero obetivo es menor")
    elif input_num<target:
        print("el numero obetivo es mayor") 
    elif input_num!=int:
        print("solo escribe numeros")       
    

