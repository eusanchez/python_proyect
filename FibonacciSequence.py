#!/usr/bin/python3


import argparse
import time

parser = argparse.ArgumentParser()

start = time.time()

def fibonacci(n):
	a, b = 0,1
	
	for i in range(n):
		a, b = b, a+b
	return b

def main():
	parser.add_argument(
		'posicion',
		type = int, 
		help = "El numero de Fibonacci del indice es: "
	)
	parser.add_argument(
        	'--tiempo', 
		"-t", 
        	action = "store_true", 
       		help = "Imprime el tiempo transcurrido para finalizar la secuencia de Fibonacci"
	)
	parser.add_argument(
        	'--completa', 
        	"-c", 
        	action = 'store_true', 
        	help = "Calcula todos los numeros de la serie hasta el numero N"
	)
	args = parser.parse_args()

	if args.completa:
		print ("La serie de Fibonacci hasta el indice: {}".format(args.posicion))
		for i in range (args.posicion+1):
			print(fibonacci(i))

	if args.posicion:
		result = fibonacci(args.posicion)
		print ("El numero de Fibonacci de indice " + str(args.posicion) + " es: " + str(result))

	if args.tiempo:
		print ("El tiempo total de ejecucion es: " + str(end - start) + " segundos.")
		 

end = time.time()
main()

#NOT RECURSIVE
