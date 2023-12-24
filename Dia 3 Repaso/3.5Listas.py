mi_lista=['a','hola','c']
milista2=['perro','gato','caballo']
print(len(mi_lista))# para saber largo de la lista
resultado=mi_lista[1]# para saber la palabra es 1 de la lista
resultado2=mi_lista[0:2] # para ver el 2 se pone el 2 porque asi lo toma
print(mi_lista)
print(resultado)
print(resultado2)
print(mi_lista+milista2)
#en la lista si se puede sobreescribir palabras eemplo cambiar gato por oso
milista2[1]='oso'
print(milista2)
#para agrepar palabras o cosas a la lista se pone .append
mi_lista.append('D')
print(mi_lista)
#para ordenar la lista pongo .sort

n1=['z','m','t','b']
n1.sort()
print(n1)
