auto= "ferrari"
numero=2
numero=str(numero)
print("mi " + auto + " " + "tiene patente " + numero)
#lo anterior solo sirve si ambos variables son un string , sino saldria error ya que numero es un int
#por lo tanto una manera mas facil de hacer esto es formateando cadenas:
#metodo 1: funcion format
print("mi auto es {} y de matricula {}".format(auto,numero))
#lo anterior es dificil de leer por lo tanto el metodo 2 es mas facil y es asi:
#Metodo 2 : Poner una f antes de las "
print(f"mi auto tiene un {auto} con patente {numero}")

#otro eemplo
x=10
y=50
z =10.5
print(f"los numeros que tengo son {x} y {y} y {z} y su suma es {x+y}")
print("los numero que tengo son {} y {} y las suma da {}".format(x,y,x+y))