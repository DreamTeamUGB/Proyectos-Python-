#/usr/bin/python
import math

def calcularNumeroPrimo(numero):	
	
	b = 0
	contador = 0
	for i in range(1, numero+1, 1):
		b = numero % i
		if b == 0:
			contador = contador + 1
	if contador <= 2:
		return "El numero " + str(numero) + " es primo."
	else:
		return "El numero " + str(numero) + " no es primo."
	

#Factorial de un numero
def calcularFactorial(numero):
	a = numero
	factorial = a
	for i in range(1, a, 1):
		factorial *= i
	
	return "El factorial de " + str(a) + " es " + str(factorial)
def calcularPalidromo(palabra):
	a = palabra[::-1]
	if a == palabra:
		return "Es palidrome"
	else:
		return "No es palidrome"
def calcualarRaizCuadrada(numero):
	return math.sqrt(numero)
	
	
	
def informacion():
	a = """\n\nSaludo este es un programa hecho para la asignatura de Desarrollo de Software Libre\n
	     Para selecciones una opcion del menu\n
	     \t -n Ingrese \"-n\" para calcular el numero primo
	     \t -f Ingrese \"-f\" para obtener el factorial de un numero
	     \t -p ingrese \"-p\" para obtener si un palabra es palidrome
	     \t -r ingrese \"-r\" para obtener la raiz cuadrada de un numero
	     Ejemplo:\n\t $python programa.py -n 7  
	     \n       Nombre\t\t\t   Codigo
	     \nMario Ernesto Flores\t\t SMiS041008
	     \nNoel Humberto Dominguez\t\t SMiS001808
	     \nKarla Marisol Colindres\t\t SMiS009108
	     \nJulio Alberto Jandres\t\t SMiS007408
	     \nAlexander de Jesus Argueta \t SMiS025408\n"""
	return a
