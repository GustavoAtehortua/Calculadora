import math
def Salir():
	global Salida
	condicion = int (input("Desea Salir? \nPara volver al menu ingrese 1 \nPara salir ingrese 2\n"))
	if (condicion == 1):
		Salida = False
	else:
		Salida = True

	
def ingreso():
	global a,b
	a = float (input("Ingrese primer numero\n"))
	b = float (input("Ingrese segundo numero\n"))
def Suma():
	print ("El resultado es: ",a+b,"\n")
	
def Resta():
	print ("El resultado es: ",a-b,"\n")
	
def Multiplicacion():
	print ("El resultado es: ",a*b,"\n")
	
def Division():
	if (b==0):
		print ("No se puede dividir en 0\n")
		
	else:
		print ("El resultado es: ", a/b,"\n")

def Raiz():
	c = float (input("Ingrese numero\n"))
	square = math.sqrt(c)
	print("El resultado es: ", square,"\n")


Salida = False
while(Salida==False):
	print ("1 Suma")
	print ("2 Resta")
	print ("3 Multiplicacion")
	print ("4 Division")
	print ("5 Raiz")
	print ("6 Salir")

	opcion=int(input("Ingrese opcion\n"))
	if(opcion==1):
		ingreso()
		Suma()
		Salir()

	elif(opcion==2):
		ingreso()
		Resta()
		Salir()

	elif(opcion==3):
		ingreso()
		Multiplicacion()
		Salir()

	elif(opcion==4):
		ingreso()
		Division()
		Salir()

	elif(opcion==5):
		Raiz()
		Salir()

	elif(opcion==6):
		Salida = True
