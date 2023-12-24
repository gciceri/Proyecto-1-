# un eemplo es queres imprimir hola en cada elemento que tengo 
nombre=["Gianca","Nicolas","Seba","Cristian"]
for elemento in nombre: 
    print("Hola")
    print("Hola "+ elemento)
 # aca me va a arroar 4 "hola" ya que tengo 4 elementos en la lista
# si quiero agregar el  hola + el nombre , tengo que poner print("Hola"+elemento)
    
lista=['a','b','c','d']
for letra in lista:
    numero_letra=lista.index(letra)+1 
    print(f"Letra {numero_letra}: {letra}")

autos=['ferrari','ford','fiat','VW','renault']
for auto in autos:
    if auto.startswith('f'):
        print(f"auto que parte con f:{auto}")
    else:
        print(f"auto que no parte con f: {auto}")   


n=[1,2,3,4,5]
mi_valor=0
for n1 in n:
    mi_valor=mi_valor+n1
    print(mi_valor)# aca me sale un valor cada loop
print(mi_valor)    # aca me sale un valor en total