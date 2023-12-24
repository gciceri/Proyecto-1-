n1=(1,2,3,4)
print(type(n1))

t=5,4.5,"perro",
print(type(t))
print(t[1])

t1=(1,2,(20,30),40)
print(t1[2][0])

#puedo asignar numero a variables o lo que sea eemplo
t2=9,3,5
x,y,z=t2
print(x,y,z)

#puedo contar las cosas que necesito
t6="giancarlo", 12,16,14,'giancarlo'
print(t6.count('giancarlo')) #hay dos giancarlo en la lista
mi_lista=list(t6)#para convertir la tuple en lista
print(type(mi_lista))