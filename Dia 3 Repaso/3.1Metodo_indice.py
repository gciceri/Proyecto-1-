# index() sirve para conocer el indice de un caracter
#va del 0 al infinito , por eemplo , hola la h seria 0 o seria 1 y asi
# un eemplo es que quiero buscar donde se encuentra la letra en un texto seria

#quiero saber en que posicion esta la letra a
palabra="hola"
resultado=palabra.index("a")
print(resultado)
palabra.index("a")
# ahora si se repiten las letras , puedo poner desde donde quiero que empiece a buscar
#se hace poniendo  index.("h",5,8) , siendo 5 que empieza a contar de esa letra y 8 que hasta esa letra
palabra2='estoy haciendo una prueba de programar'
resultado5=palabra2.index("a",9,20)
print(resultado5)

#ahora quiero buscar que letra esta en tal posicion y es con []
resultado2=palabra[2]
print(resultado2)
#ahora si quiero que sea de izq a derecha siempre se utilza -1 -2 siendo
# siendo -1 el a -2 la l -3 el h pero 0 siempre sera el primero , osea h
resultado3=palabra[-3]
print(resultado3)