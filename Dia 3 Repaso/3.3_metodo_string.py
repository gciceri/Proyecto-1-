#aprender 6 metodos a usar
#upper() para pasar un string a mayuscula
#lower() para pasar a minuscula
#split() para separar y poner un string entero en lista de palabras
#join() unir items usando separador
#find() encontrar un substring
#replace() reemplazar un substring

n1="hola, soy Giancarlo y Estoy programando"
n2=n1.upper()
print(n2)

#split
resultado=n1.split()
print(resultado)
# lo que hace aca es hacer un listado con las palabras cuando no hay espacio
resultado2=n1.split("o")
print(resultado2)
#lo que hace aca es hacer un listado usando al o como separador

#join
a= "aprender"
b= "python"
c= "estoy aprendiendo"
n4=" ".join([a,b,c])
print(n4)
#se pone pone ese espacio en la comilla para asi hacer que alla una separacion entre palabras

#find
resultado5=n1.find("Giancarlo")
print(resultado5)

#replace
result=n1.replace("programando","programanding")
print(result)
result2=n1.replace("programando","programando en python")
print(result2)