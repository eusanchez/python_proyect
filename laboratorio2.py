
#!
# Ana Eugenia Sanchez Villalobos, este programa se basa en recibir nombres de personas y poder escribirlos con sus debidas mayusculas. 
# version 5.2.38
lista  = [] 
while (True):
	x = str(input("Escriba el nombre que desea procesar, o SALIR para salir: "))
	y = x.split()
	tamlista = len(y)
	if (x=="SALIR"):break
	lista.append(x)
	if (tamlista<=2) or (tamlista>=5):
		lista.remove(x)
		print ("ERROR: debe digitar nombres de 3 o 4 componentes")
	resultado = ('\n'.join(lista))
print (resultado.title()) 


