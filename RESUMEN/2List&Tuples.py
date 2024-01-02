#listas
materias=['Calculo','Finanza','Macroeconomia','Historia']
print(materias)
print(materias[2]) # para buscar el 3 elemento de la lista
print(materias[-1])
print(materias[0][-1])#para llegar al ultimo caracter del primer elemento. buscamos la primera palabra [0], luego otra [-1]con el ultimo caracter

#con la funcion len podemos ver cuandos elementos hay en la lista
print(len(materias))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#para sumar los elementos
sumar=sum([1,2,3,4,5])
print(sumar)
#para ordenarlos seria con sorted
print(sorted([4,6,1,3,9,1,1,0]))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#INDICES
# A diferencia de un str o una lista, permite obtener, asignar, reemplazar, elimianr valores dentro de una lista
#primer elemento lista
print(materias[0])

#puedo asignar el primer elemento de una lista
materias[0]="Finanza"
print(materias[0])
#eliminar del 2do al 3er elemento de la lista
print(materias)
materias[1:3]=[]
print(materias)

#La lista puede tener cualquier tipo de obeto
lista=["pi",3.14,['alfa','beta'],12]
print(lista[2][0])#imprile el 3 elemento de la lista y luego el primer elemento dentro de la lista nueva. si le agrego otro []me lanza el caracter

# CONCATENAR 2 LISTAS
matematicos=["Gauss",'Spivak',"Fermat"]
fisicos=["Newton",'Maxwell']
cientificos=matematicos+fisicos 
print(cientificos)

#COPIAR LISTA
print(id(cientificos)) #Cada elemento en python se identifica con un unico ID
cientificos2=cientificos
print(id(cientificos2)) # tiene el mismo ID (ya que die que eran lo mismo) y si agrego algo  a cientificos 2 tambien cambiara en el otro
cientificos2[0]="Hola"
print(cientificos) # HASTA ACA PODERMOS VER QUE SON IGUALES. AHORA COPIARESMOS LA LISTA Y TENDRA DIFERENTE ID CADA UNA

cientificos3=cientificos[:]
print(id(cientificos), id(cientificos3)) #tienen diferente ID ya que copie los elementos de la lista 
cientificos3[0]="Giancarlo"
print("Lista 'Cientificos 3\n", cientificos3) ; print("Lista 'Cientificos\n'", cientificos)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Metodo de un list 
lista2=['a','b','c','d']
print(lista2)
#para hacerla al reves
lista2.reverse()
print(lista2)
#PARA AGREGAR ALGO SE PONE .append
lista2.append("e")
print(lista2)

# ahora para insertar algo nuevo en alguna posicion
lista2.insert(0,"aa")
print(lista2)
#para buscar algo INDEX
print(lista2.index("d"))
print(sorted(lista2))
lista2.sort() #sirve para ordenar alfabeticamente el de arriba tambien
print(lista2)

# list.pop: obtiene el ultimo elemento de la lista y lo elimina
print(lista2.pop()) # aca imprime lo que elimino
print(lista2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#hacer un split de un string
print("este es un split".split())  # esto es para pasar de un STR a una LISTA
lista4=["Esto","es","una","lista"]
print(" ".join(lista4))


#eercicios
# considera la lista numero0 y calcula el valor promedio
numero0=[1,1,2,3,5,8,13]
print((sum(numero0)/len(numero0)))
#imprimir la suma del primer elemento, el ultimo y el del medio de la lista
numero1 = [0, 7, 20, 11, 1, 17, 4, 13, 9, 0, 12, 18, 5, 10, 8, 0, 10, 6, 19, 19, 10, 9, 4, 4, 18, 18, 0]
lista_num1=[numero1[0],numero1[-1],numero1[int(len(numero1)/2)]]
print(sum(lista_num1))

list1 = ["a", "b", "a", "d", "a", "a", "c"]
print(" ".join(list1).replace('a','*').split())
#arriba , converti la lista en un string, luego cambie las letras de 'a' a '*' y luego converti el str en una lista con .split()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# TUPLE A DIFERENCIA DE LA LISTA VA CON () 
#EEMPLO TUPLE
strike1=10
strike2=15
strike3=29
# tambien puedo poner
strike1,strike2,strike3=10,15,29
print(strike1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Diccionarios
alumnos={
"Nicolas":[11,"azul","administracion"],
"Giancarlo":[25,"azul","finanza"],
"Paolo":[50,"amarillo","publicidad"],
"Luis":[23,"negro", "adm"],}
print(alumnos)
#para sacar un elemento del diccionario pongo del 
del alumnos["Luis"]
print(alumnos)
#para agregar pongo alumnos["Luis"]=[]
alumnos["Guillermo"]=[21,"cafe","pulicidad"]
print(alumnos)

#DENTRO DE UN DICCIONARIO
print(alumnos.keys())
print(alumnos.items())

vocales={"a","e","i","o","u"}
p1={"a","w","d","e"}
print(vocales&p1) # & interseccion , que tienen entre los 2
print(vocales|p1) #unir elementos 
print(vocales-p1) # elementos en vocales no presentes en P1
print(vocales^p1) # elementos en A o B pero que no estan en los 2












