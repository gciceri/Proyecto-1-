#relacionr loops funciones y if elif else 

def chequear_3_cifras(numero):
    return numero in range (100,1000)

resultado= chequear_3_cifras(647)
print(resultado)

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return true 
        else:
            pass

resul=chequear_3_cifras(55,200,1000)

