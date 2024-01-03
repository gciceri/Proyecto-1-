#BOOLEANOS EN PYTHON
#programa de computacion toma decision en terminos binarios True or False 
# ==: Equivalencia
# !=: Diferencia
# not: Negación
# and: y
# or: o

my_str="The Tipping Point"
print(my_str.endswith("boolean"))#False
print(my_str.endswith("Point"))#True

###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#USOS IN
print("Tipping" in my_str) #TRUE
print("one" in ["one","two","three"]) #TRUE
print("five" in ["one","two","three"])#FALSE

#COMPARACIONES LOGICAS
print(3>5) #false
print(3<5)#true
print(3<=5)#true
print(4==1)#false
print(4!=5)#true

#eercicios

x=5
print(3<x and x<10) # es verdadero

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# IF

lista_usuarios = ['usr186', 'usr203', 'usr919', 'usr989',
                  'usr587', 'usr131', 'usr640', 'usr757',
                  'usr237', 'usr491']
usuario=input("Ingresa tu Usuario: ")
if usuario in lista_usuarios:
    print("Hola ", usuario)
else: print("No eres usuario")   

#ELIF sirve para otra cosa eemplo 
lista_usuarios_bloqueados = ['usr160', 'usr464', 'usr461',
                             'usr737', 'usr835', 'usr491']
if usuario in lista_usuarios_bloqueados:
    print("Este usuario esta bloqueado")
elif usuario in lista_usuarios:
    print("Hola usuario")
else:print("no eres usuario")       

temperatura=int(input("Que temperatura hay?: "))
if temperatura >= 35:    print("Hace mucho calor") 
elif temperatura<-15 : print("Hace mucho frio")
elif temperatura > 25  and temperatura <35:
    print("Hace Calor")
elif temperatura>=15 and temperatura<12:
    print("el clima es templado")    
elif temperatura >=12 and temperatura<=25:
    print("el clima es templado")


   #EEMPLO 
user_pass = {'usr503': '2vu2bo',
 'usr085': 'geeaa',
 'usr406': 'xqzbiy',
 'usr182': 'jbngo0',
 'usr168': 'qih6e',
 'usr900': '6ynym',
 'usr542': '7p6mnd',
 'usr847': 'ruqq6y',
 'usr629': '9qs9g5',
 'usr418': 'f15lg'}

inicio=input("Ingresa su Usuario: ")

if inicio in user_pass:
    print("Usuario Registrado")
else:
    opciones_registro=input("Su usuario no esta registrado, Desea Incribir? S/N: ")
    if opciones_registro=="S" or opciones_registro=="s":
           contrasena=input('Escriba su contrasena: ')
           user_pass[inicio]=contrasena
           print("Ha sido registrado exitosamente")
           
    elif opciones_registro!= "S" or opciones_registro!="N":
        print("Respuesta no valida, Saliendo del programa") 
    elif opciones_registro == "N":
        print("Saliendo del programa...")
print(user_pass)        
       

    
    
    
           