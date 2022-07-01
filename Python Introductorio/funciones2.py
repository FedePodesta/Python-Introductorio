#LAS FUNCIONES LE DAN UN NOMBRE A UN BLOQUE DE CODIGO, PARA LUEGO LLAMARLO Y CON ESO NO REPETIMOS CODIGO FUENTE QUE HAGA LO MISMO.

####### CREACION DE UNA FUNCION
#### def nombre-de-la-funcion (parametros):
#		sentencias
##### EJECUCION O LLAMADA DE UNA FUNCION

# nombre-de-la-funcion ()

###### EJEMPLO

'''
def perdi():
	print ("GAME OVER")
	print ("hiciste muchos puntos, pero estas fuera")
	
	
perdi()
'''


#### otro ejemplo



#def multiplicar():
#	print (2*2)
#	print("hola")
#	print(10/5)
	
#multiplicar()
#multiplicar()


#### EJERCICIO--- ARMAR UN JUEGO DONDE DENTRO
#DE UN RANGO DE NUMEROS TENGAMOS TRES OPCIONES PARA ELEJIR
# CUAL ES EL NUMERO CORRECTO

ganador = 3

def jugar ():
		contador=1
		while contador < 4:
			sel = int(input("ingrese un valor del 1 al cinco"))
			if sel != ganador:
				contador+=1
				print ("la seleccion no es la correcta y has perdido una vida. Te quedan ", 4-contador, " vidas")
				if contador ==4:
					print ("GAME OVER")
					break
				
			else:
				print ("GANASTE")
				break
			

#while True:
#	seguir_jugando=input("quiere JugaR (s/n)")
#	if seguir_jugando=="s":
#		jugar()
#	else:
#		print ("Chau, Buen día")
#		break

#jugar()
'''

'''
'''

######## argumentos de funciones. Variables que solo existen dentro de una funcion.
#### El valor de los parametros solo lo tienen dentro de la funcion,
### el valor de los parámetros son asignados cuando se llama a la funcion. 

'''
'''
'''
#a=10

#def imprimir_suma(z=10, pepe=20):
#	 print("Resultado:")
#	 print(z + pepe)
#	 print(z)

#imprimir_suma() 
#print(a)


#imprimir_suma(-5, 3.5) #a= -5  b= 3.5

#def sumar (argumento1,argumento2):
#	print (argumento1+argumento2)






'''

def restar (argumento1,argumento2):
	print (argumento1-argumento2)
def multi (argumento1,argumento2):
	print (argumento1*argumento2)
def dividir (argumento1,argumento2):
	print (argumento1/argumento2)


while True:
	numero1= int(input("ingrese un numero"))
	numero2= int(input("ingrese un numero"))
	seleccion= int(input("seleccione 1) Sumar , 2)Restar, 3)Multiplicar, 4)Dividir, 5) Salir"))
	if seleccion == 1:
		sumar(numero1,numero2)
	elif seleccion ==2:
		restar(numero1,numero2)
	elif seleccion ==3:
		multi(numero1,numero2)
	elif seleccion ==4:
		dividir(numero1,numero2)
	else:
		print ("chau")
		break

'''
'''
def sumar (argumento1 = 10,argumento2= 20):
	print (argumento1+argumento2)
'''
#def sumar (argumento1, argumento2):
#	print (argumento1+argumento2)
	
#sumar() 
'''
####### el orden de los argumentos es importante pero se pueden cambiar y no respetar el orden haciendolo explícito
#sumar(argumento2=5,argumento1=7)        ##### valores por defecto.

'''
'''

#'''

###VOLUMEN DE UNA ESFERA   4/3*PI*RADIO**3

#def volumen_esfera (radio):
#	PI= 3.14
#	volumen=(4/3)*PI*radio**3
#	print ("el volumen de la esfera es: ", volumen)
	#return volumen

#print (volumen_esfera(33))
	
#def f (argumento):
#		total = 10 + argumento
#		return total
#valor = volumen_esfera(33)
#print(f(valor))



'''
'''

#funciones con varios parámetros
#### volumen del cilindro    PI *radio**2*altura
'''
'''
#def volumen_cilindro(arg1,arg2):
#	PI= 3.14
#	print ("El volumen del cilindro es: ", PI*arg1**2*arg2)


#radio= float(input ("ingrese el radio del cilindro"))
#altura= float (input("ingrese la altura del cilindro"))

#volumen_cilindro(radio,altura)


### valores de retorno de una funcion  -------- parabra reservada "return"
####  el resultado de una funcion es asignar a una variable


#def sumamos (numero1,numero2):
#	suma=float(numero1+numero2)
	#print (suma)
#	return suma

#a=sumamos(10,30)

#a=sumamos(10,5)

#print(a)

#total= sumamos(3,5)+sumamos(7,5)
#print(total*1.21, "es el total mas iva")

### ejemplo con error
#print (suma)   #### la variable está definida dentro de la funcion y no puede acceder, solo por el return
'''
'''
'''
sumamos(10,9.5)
print ("no se imprimió nada")

print (sumamos(10,9.5))
'''
####### otro ejemplo de retorno
'''

vida="hola"
edad= 20

def control_edad ():
	edad = int(input("ingrese su edad"))
	if edad <= 12:
		vida="muy saludable"
	elif edad > 50:
		vida="a cuidarse"
	else:
		vida="saludable"
	return vida

print(control_edad())

#print(edad)
##print(vida)


#variable = control_edad()
#print (variable)
	
'''	

### volumen del cilindro   PI*r**2*h    ---- DOS PARAMETROS..... RADIO Y ALTURA




