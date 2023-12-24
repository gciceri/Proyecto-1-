

texto='ABCDEFGHIKLMNOP'
fragmento=texto[2]
print(fragmento)
fragmento2=texto[2:5]
print(fragmento2)
# el anterior significa que me agarra del caracter 2 hasta el 5
#ahora si pongo [2: ] , significa que me agarra desde el caracter 2 hasta el final
fragmento3=texto[2:]
print(fragmento3)
# si hago [2:3:3] , significa que me va a ir tomando de cada 3 caracteres
fragmento4=texto[2:10:2]
print(fragmento4)