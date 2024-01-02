#relacionr loops funciones y if elif else 

def chequear_3_cifras(numero1):
    return numero1 in range (100,1000)

resultado= chequear_3_cifras(647)
print(resultado)

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True 
        else:
            pass


