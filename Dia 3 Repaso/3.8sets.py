#coleccion de elemento
#se puede hacer de 2 formar

#1
set({1, 2, 3, 4, 5})
#2
{1,2,3,4,5}

mi_set=set([1,2,3,4,5])
print(mi_set)

otroset={1,2,"g"}
print(otroset)
#se puede unir todo con . unir
s2=mi_set.union(otroset)
print(s2)
#para agregar
s2.add(54)
print(s2)

si.pop() # sirve para eliminar algo de forma aleatoreo
s1.clear()# es para vacear el set