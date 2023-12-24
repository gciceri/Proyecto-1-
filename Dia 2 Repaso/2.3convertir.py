num1=20
num2=30.5
print(type(num2))
num1=num1+num2
#la suma de lo anterior va a ser un float ya que es un numero decimal la suma
#para hacer que sea un integer tenemos que hacer
num3=int(num1)
print(type(num3))
print(num3)
#lo que hace es que elimina los decimales porque lo convierte en un entero

edad=input("dime tu edad: ")
print(type(edad))
edad=int(edad)
print(edad + edad)
print(type(edad))

#ahora se pudo smar las edades porque se sumo dos integers

#entonces hagamos que tenemos un numero num4 = 7.5 y num 5= 10 que quiero que se sumen
num4=7.5
num5=10
print(num4+num5)
print(float(num4)+float(num5))