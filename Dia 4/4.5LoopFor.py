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
    