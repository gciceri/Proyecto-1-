#consiste en que si se cumple una condicion o no , python eecuta un codigo 
# eemplo: si se encuentra X dato muestramelo , sino muestrame error
#palablas claves : IF , ELIF  ELSE 


if 10>9:
    print("es correcto")

if 5==2:
    print("es correcto")
else:
    print("no es correcto") 

mascota="perro"
if mascota== "gato":
    print("es correcto")
else:
    print("es incorrecto")

edad=16 
calificacion=9 

if edad<18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("estas aprobado")
    else:   
        print("estas desaprobado")
else:
    print("eres adulto")            



    