mi_lista = ['a','b','c']
lista2 = ['d','e','f']
n1 = mi_lista[0: ]
print(mi_lista+lista2)
lista3= mi_lista+lista2

#sobre escribir solo en el primer indice
lista3[0]= 'alfa'
print(lista3)

#para agregar elemento a la lista tengo que poner .append
lista3.append('hola')
print(lista3)

#para remover lo ultimo d ela lista tengo que poner .pop al nocer que ponga .pop[]
lista3.pop(0)
print(lista3)

#para ver el elemento eliminado
eliminado=lista3.pop(2)
print(lista3)
print(eliminado)