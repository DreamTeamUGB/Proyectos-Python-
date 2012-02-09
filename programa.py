#!/usr/bin/python
import sys
import math
from metodos.metodo import *

try:
	
	if len(sys.argv) >= 2:
		if sys.argv[1] == "-n":
			numero = int(sys.argv[2])
			print calcularNumeroPrimo(numero)
		elif sys.argv[1] == "-f":
			numero = int(sys.argv[2])
			print calcularFactorial(numero)	
		elif sys.argv[1] == "-p":
			palindrome = calcularPalidromo(sys.argv[2])
			print palindrome
		elif sys.argv[1] == "-r":
			raiz = int(sys.argv[2])
			print calcualarRaizCuadrada(raiz)
		elif sys.argv[1] != "-n" and sys.argv[1] != "-f":
			print informacion()	
	else:		
		print informacion()
			
except ValueError:
	print "Hubo un error al ingresar el numero"
