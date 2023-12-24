nombre= input("esribe tu nombre: ")
ventas = input('escribe el total de tus ventas: ')
ventas= int(ventas)
comision= ventas*13/100


print(f"hola {nombre}, tus comisiondes de este mes son {comision}, felcidades")

print("se usa int porque el numero de las ventas es un numero entero, sino se ocupar float al usar decimal")