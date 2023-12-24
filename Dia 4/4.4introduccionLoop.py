#sirve para que un bloque de codigos se eecute mas de una vez o las veces que sea necesario
#loop for se usa apra n veces y loop while para infinitas veces
#loop FOR
lista=["a",'b','c']
for letra in lista:
    numero_letra=lista.index(letra) +1
    print(letra)
    print("letra: " + letra)
    print(f"Letra {numero_letra}: {letra}")

ingrediente=['pollo','arroz','carne','queso']
for insumos in ingrediente:
    numerodeingr=ingrediente.index(insumos)+1
    print(f"El numero de este ingrediente '{insumos}', es el {numerodeingr}")
    print(insumos)

autos=["ferrari","maserati","alfa romero","ford"]
for marcas in autos:
    posicionauto=autos.index(marcas)+1
    if marcas.startswith("f"):#solo me va a imprimir las que partan con f
        print(f"la marca de auto que hay es el {marcas} y la posicion es {posicionauto}")
