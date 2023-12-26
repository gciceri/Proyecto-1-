#se repite mientras(while) se repite una condicion hasta la condicio que se le pone 
#palabras claves Break, Continue , Pass

monedas=5
while monedas > 0: 
    print(f" tengo { monedas} monedas")
    monedas = monedas -1 
else: print("No tengo mas dinero")    

respuesta= 's'
while respuesta == 's':
    respuesta= input('quieres seguir? (S/N)')
else: print('gracias')

