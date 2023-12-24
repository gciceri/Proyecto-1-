diccioario={'c1':'valor1','c2':"valor2"}
print(diccioario)
#ahora queremos consultar lo que hay en alguna clave
resultado=diccioario['c1']
print(resultado)

#eempllo
cliente={'Nombre':"Giancarlo","apellido":"Ciceri","numero":7}
consulta=(cliente['apellido'])
print(consulta)

dic={'c1':['a','b','c'],'c2':['der','e','f']}
print(dic['c2'][0].upper())
#para agregar cosas a un diccionario es
dic1={1:'a',2:'b'}
dic1[3]='c'
print(dic1)
#para sobreescribir se hace por eemplo cambiar la a por una z es
dic1[1]="z"
print(dic1)

#para ver las claves , que serian las listas [] ponemos
print(dic1.keys())
#para ver los valores seria poner .value()
print(dic1.values())
