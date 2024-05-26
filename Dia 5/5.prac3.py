#verifica si los sets a continuacion forman conuntos aislados ( es decir que no tienen elementos en comun)

marcas_smartphone= {'samsung','xiaomi','apple','lg'}
marcas_tv={'sony',"phillips",'samsung','lg'}
a=marcas_smartphone.isdisjoint(marcas_tv)
print(a)
# resultdo falso, ya que si se repiten 