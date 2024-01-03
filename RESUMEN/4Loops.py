lista={"giancarlo":[12],
       "Tomas":[15]}

new=input("nombre")
if new in lista:
    print("ya esta registrado")
else:
    registro=input("no esta registrado. desea registrarse S/N")
    
    if registro == 's' or registro=="S":
        contrasena=input("escriba contrasena")     
        print("se a registrado con exito")
    elif registro != "n":
        print("usuario no registrado")



    