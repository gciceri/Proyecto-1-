#loop 
#es cuando tenemos un bloque de codigos que queremos repetir un numero finito de veces 
#eemplo , queremos calcular el area de: a=pi*r^2, de numero n de circulos
# dada la lista de radios
radios=[1,3,5,2,1,10]
pi=3.14159265
# se se puede hacer esto copiando cada radio con pi pero nos podemos equipocar, entonces
# USAMOS FOR 
for radio in radios:
    print(pi*radio**2)
print("son todos los elementos") 

for radio in radios:
    print(pi*radio**2)
    print("espacio entre radio")
print("son todos los elementos") 

word="beseechigly"
for letter in word:
    print(letter)

for n in range (5):
    print(n+1)

for n1 in range (4,12,2):
    print(n1) 

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#WHILE

x=1
while x <=10:
    print(x,end=" ")
    x=x+1

#a veces es importante romper el loop con break

#comidas=[]
#print("ingresa las comidas que te gusten. Escribe 'fin' para terminar")
#while True:
#    comida=input("comida: ")
#    if comida != "fin":
#        comidas.append(comida)  
#    else:
#        print("saliendo del programa")    
#        break   
  

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#agrupando elementos con Zip 

tickers = ["AAPL", "AMZN", "FB", "GOOG"]
companies = ["Apple", "Amazon", "Facebook", "Alphabet"]
comp_tick = {} # diccionario para guardar valores
for ticker, company in zip(tickers, companies):
    comp_tick[company] = ticker
    
print(comp_tick)

#eercicios

#eercicio 2

radios1=[2,3,4,10,23,45,64,23,65,23]
for radio12 in radios:
    circulo=round(radio12**2*pi,3)
    print(f"el area del ciruclo es {circulo}")

print("fin eercico 2 ")

# eercicio 3 
print("\nEercicio 3 ")

y=1
while y<=5:
    print(y,end="\n")
    y=y+1
    
    














    