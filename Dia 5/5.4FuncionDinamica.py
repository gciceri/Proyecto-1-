#relacionr loops funciones y if elif else 

def chequear_3_cifras(numero1):
    return numero1 in range (100,1000) 

resultado= chequear_3_cifras(647) # Hice funcion para crear algo que me dice si tiene 3 cifras el numero 
print(resultado)

def chequear_3_cifraslista(lista): # ahora veremos los elementos que hay en un y si es verdad que algun elemento tiene 3cifras
    for n in lista:
        if n in range(100,1000):
            return True 
        else:
            pass # se pone pass para que siga con el siguiente numero hasta encontrar un TRUE , si pongo RETURN FALSE corta al primer FALSE 
    return False    
         # se poner false aca para que finalice si no tiene nada 

resultado=chequear_3_cifraslista([99,1202,10000]) # es verdadero porque alguno de la lista tiene 3 cifras

print(resultado)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def chequear_3_cifraslista(lista):  # ahora haremos un lista para guardar los numero con 3
    
    lista_3_cifras=[]
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
            
        else:
            pass # se pone pass para que siga con el siguiente numero hasta encontrar un TRUE , si pongo RETURN FALSE corta al primer FALSE 
    return lista_3_cifras   
         # se poner false aca para que finalice si no tiene nada 

resultado=chequear_3_cifraslista([99,122,10000]) # es verdadero porque alguno de la lista tiene 3 cifras

print(resultado)


def guardar_numeros(lista):
    
    guardar_aca=[]

    for numeros in lista:
        if numeros in range(1,1000):
            guardar_aca.append(numeros)
        else: pass
    return print(guardar_aca)        

guardar_numeros([1,2,3,4,5,999])


# PRACTICO1

print("\nPRACTICO 1 ")


lista_numeros=[1,2,5,4,5]
def todos_positivos(lista):

    for n in lista:
        if n>0:
            pass
        else: 
            return False
    return True  
print(todos_positivos(lista_numeros),"\n") 

print("PRACTICO 2 ")

def suma_menores(lista):
    suma=0 # aca le decimos python que iniciara la suma con 0 

    for num in lista:
       if num in range(1,1000):
           suma+=num #significa que sumara los numeros num sumado al 0
    return suma       
print(suma_menores([2,2,2,2,-1]),"\n")

print("PRACTICO 3")






    
       

   
  
  









    



