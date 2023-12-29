#Random 
#para hacer esto hay que importar una libreria
from random import *
aleatorio= randint(1,5)
print(aleatorio)

a= uniform(1,3)# uniform vaa tirar un valor decimal entre el 1 al 5
print(a)
b= random()
print(b) #cualquier decimal entre 0 y 1 

colores=['azul','roo','blanco','negro']
c=choice(colores)
print(c)

numeros=list(range(5,50,3))
shuffle(numeros)# esto hace que los numeros se pongan aleatorios
print(numeros)
