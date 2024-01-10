from random import *
radios = [1, 3, 5, 2, 1, 10]
pi=3.14159

for radio in radios:
    print(pi*radio**2) #pongo radio ya que abarca a todos los radios
    print("") #si pongo este va a ver un espacio entre cada radio
print("finalizado")   

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Rango

# range(a) crea un rango de valores de 0 hsta a-1
# range(a, b) crea un rango de valores de a hasta b-1
# range(a, b, s) crea un rango de valores de a hasta b-1 dando saltos s

for n in range(5):
    print(n) # va a imprimir numero del 0 al 4 hacia abao 
print("\n")    
for n1 in range(5,11):
    print(n1) # va a imprimir del 5 al 10 hacia abao
print('')    
##>>>>>>>>>>>>>>>>>>>>>>>>>>
    
print("While")

x=1
while x <=10:
    print(x,end="")
    x=x+1
print("")

comidas=[]
print("Escribe tus comidas y si no sabes mas, para finalizar pon 'fin' ") 

# while True:
#     comida=input("escribe tu comida: ")
#     if comida != "fin":
#         comidas.append(comida)
#     else:
#         print("Saliendo del programa")    
#         print(comidas)
#         break
# print("\n")

#Agrupado Con Zip
print("ZIP")

tickers = ["AAPL", "AMZN", "FB", "GOOG"]
companies = ["Apple", "Amazon", "Facebook", "Alphabet"]
grupo={}
for ticker,company in zip(tickers,companies):
    grupo[ticker]=company
print(grupo)
##>>>>

print("\nEercicios\n")

radios1 = [69, 24, 61, 27, 93, 67, 16, 66, 79, 3, 84, 4, 2, 82, 17, 88, 1, 74, 65, 4, 82, 3, 21, 12, 62, 9, 96, 68, 63, 88]
for radio2 in radios1:
    area=pi*radio2**2
    print(f" El area del circulo con {radio2} es ",round(area,2))
print("\n\n")
#eercicio 2 

print("Eercicio 2")
for fila in range(1,6):
    for columna in range(1,fila+1):
        print(columna,end=" ")
    print("\n")     

print("eecicio 3\n")

# numero=randint(1,10)
# while True:
#     input_num=int(input("Elige un numero del 1 al 100: "))
#     if input_num == numero:
#        print("adivinaste")
#     elif input_num<numero:
#        print("el numero es mayor")
#     elif input_num>numero:
#        print("el numero es menor")
#        break
# print("Adivinanste!\n\n") 

print("eercico 4")

capitales = ['Aguascalientes', 'Mexicali', 'La Paz', 'Campeche', 'Saltillo', 'Colima',
             'Tuxtla Gutiérrez', 'Chihuahua', 'Ciudad de México', 'Durango', 'Guanajuato',
             'Chilpancingo', 'Pachuca', 'Guadalajara', 'Toluca', 'Morelia', 'Cuernavaca', 
             'Tepic', 'Monterrey', 'Oaxaca', 'Puebla', 'Querétaro', 'Chetumal', 'San Luis Potosí',
             'Culiacán', 'Hermosillo', 'Villahermosa', 'Ciudad Victoria', 'Tlaxcala', 'Xalapa',
             'Mérida', 'Zacatecas']
estados = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila',
           'Colima', 'Chiapas', 'Chihuahua', 'Distrito Federal', 'Durango', 'Guanajuato',
           'Guerrero', 'Hidalgo', 'Jalisco', 'México', 'Michoacán', 'Morelos', 'Nayarit',
           'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí',
           'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']

agrupar={}
for capital,estado in zip(capitales,estados):
    agrupar[capital]=estado
    print(f"la capital de {capital} ,{estado}")
print("\n\n\nEercicio5")
               


 


    
    

        


