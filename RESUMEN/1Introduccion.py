#para buscar que tipo es poner type()
print(type('hola mundo')) # sabe que es un string

# podemos separar una frase en diferentes parrafos con \n
print("hola\nmundo")
#tambien podemos poner """ tres comillas
print("""hola 
      mundo""" )

#para saber el largo de la palabra
print(len("python"))

print("z"*50) # imprime 50 veces z

# si pongo .title() , pone las primeras de cada palabra en mayuscula
print("machine learning".title())

#si quiero poner toda la palabra en mayuscula .upper()
print("mayuscula".upper())
#todas en minuscula .lower()
print("MINUSCULA".lower())

#quitar espacio innecesario .strip()
print("este string tiene espacio innecesario      ".strip())

#para buscar .find()
print('una gran maquina'.find("gran"))
# si no esta da como resultado -1

#para remplazar se pone .replace("gran","pequena")
print('una gran maquina'.replace('gran','pequena'))

#llegar al ultimo caracter del string 
print("ultima"[-1])

#slicing para obtener corte sucesivo
#"slicing"[ini:fin]
print("python"[1:4]) #el 4 elemento lo cortara
#tambien se puede 
print("python"[:-4])

# int y float
print(type(4)) # este es un integer
print(type(4.0)) #este es un float

#funciones numericas
print(round(3.1123123,4)) #redondear
print(max(3,4,5,-1,9,8)) # numero maximo

nombre='giancarlo'
print(f"Hola, {nombre}")
print("Hola, ", nombre)
print("Hola, " + nombre)

#EERCICIO

#CACLULAR VALRO PRESENTE CUPON ZERO CON VALOR
#VALOR NOMINAL C=100 , i=7% VENCIMIENTO T=10 ANOS
c=100
i=0.07
t=10
vp=c/(1+i)**t
print(vp)

c_inm=float(input("escribe el valor nominal del cupon"))
i_inm=float(input("escribe la tasa a la cual estara el cupon"))
t_inm=float(input("cuantos anos sera?"))
B=c_inm/(1+i_inm)**t_inm
print(B)

name=str(input("cual es tu nombre "))
edad=int(input("cual es tu edad "))
print((name +"\n")*edad)

print((name + '\n') * edad)
print(f"{name}\n"*edad)

trabalenguas = """En tres tristes trastos de trigo,
tres tristes tigres comían trigo.
Comían trigo, tres tristes tigres,
en tres tristes trastos de trigo."""
# eliminar todas las r y s del string

print(trabalenguas.replace("r","").replace("s",""))

a=input("pon tu nombre")
b=int(input("pon tu edad"))
print(f'{a}\n'*b)

name=input("escribe tu nombre: ").strip()
first,last=name.split(" ")
print(last)
