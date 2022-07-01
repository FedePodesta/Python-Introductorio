'''
REPASO
INTRODUCCION A LA PROGRAMACION
INSTALACION DE INTERPRETE DE PYTHON python.org

INSTALACION DE GEANY. USO DE HERRAMIENTAS IDE (Geany, visual studio code, pycharm, athom, spider, etc......)

print ("HOLA MUNDO")
CONSOLA O TERMINAL DE WINDOWS (CMD)
VARIABLES - DECLARACION DE UNA VARIABLE
'''
'''
velocidad = 10
PI=3.1415
### TIPOS DE VARIABLES

#int - enteros
#float - decimales
#str - string - caracteres
#bollean - booleanos - True - False
#funcion type()
'''
'''
'''
'''
a=10
b="hola"
c= True
d= 2.5

print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''

'''
# operaciones aritmeticas : + - / * ** // %

print ("suma: ",10+3.5)
print ("division: ",10/3)
print ("potencia: ",2**3)
print ("módulo: ", 10//3)
print ("resto: ", 10%3)


'''

'''
#concatenar strings
nombre= "Carlos"
apellido = "Perez"

print (nombre+apellido)
print (nombre*3)

'''
'''
#operadores logicos
#and
'''

verdadero = True
falso = False

'''print("operador verdadero and verdadero: ", verdadero and verdadero)
print("operador verdadero and false: ", verdadero and falso)
print("operador falso and verdadero: ", falso and verdadero)
print("operador falso and falso: ", falso and falso)

'''
#or

#print("operador vedadero or verdadero: ", verdadero or verdadero)
#print("operador verdadero or falso: ", verdadero or falso)
#print("operador falso or verdadero: ", falso or verdadero)
#print("operador falso or falso: ", falso or falso)

'''
'''

'''
#condicionales if


##if "condicion":
	###"codigo fuente" #### ojo con la indentación


temperatura = 10

if temperatura < 10:
	print("hace frío")
else:
	print ("hace calor")
	
## elif

if temperatura < 10:
	print("hace frio")
elif temperatura > 20:
	print ("hace calor")
else:
	print ("templado")
	

'''
'''
#### if anidados
temperatura = 31
humedad = 90
if temperatura > 30:
	print ("hace calor")
	if humedad > 89:
		print (" Hace calor y puede llover")
	else:
		print ("no llueve")
else:
	print ("no hace tanto calor")

'''

'''
#### condicional comparando textos

usuario="admin"

if usuario == "admin":
	print ("tiene acceso al sistema")
else:
	print ("Acceso denegado - usuario erroneo")
	
'''
#### Entrada de datos
### funcion input()
'''
usuario = input("ingrese un usuario: ")
if usuario == "admin":
	print ("tiene acceso al sistema")
else:
	print ("Acceso denegado - usuario erroneo")
	
####### ingreso de datos por entrada standart y conversion
'''
'''
temperatura = float(input("ingrese una temperatura: "))
humedad = float(input("ingrese una humedad"))

if temperatura > 30:
	print ("hace calor")
	if humedad > 89:
		print (" Hace calor y puede llover")
	else:
		print ("no llueve")
else:
	print ("no hace tanto calor")


'''
'''
##### Bucles
#for y while
# bucle while - cicla hasta cumplir una condicion
#while con condicion booleana
'''
'''
while True:
	temperatura = float(input("ingrese una temperatura: "))
	humedad = float(input("ingrese una humedad"))

	if temperatura > 30:
		print ("hace calor")
		if humedad > 89:
			print (" Hace calor y puede llover")
			break
		else:
			print ("no llueve")
	else:
		print ("no hace tanto calor")

# while con evento
'''

'''
temperatura=1

while temperatura > 0:
	temperatura = float(input("ingrese una temperatura: "))
	humedad = float(input("ingrese una humedad"))

	if temperatura > 30:
		print ("hace calor")
		if humedad > 89:
			print (" Hace calor y puede llover")
			#break
		else:
			print ("no llueve")
	else:
		print ("no hace tanto calor")

'''
'''
'''
'''
###### for - recorre listas
lista = [1,2,3,4]
print (lista)
print (type(lista))
print (lista[0])
print (lista[3])

for i in lista:
	print ("hola mundo")
	
###### for con un contador

for i in lista:
	cuenta = i +1
print (cuenta)

# cantidad de elementos de una lista
print ("La cantidad de elementos de la lista es de: ",len(lista))
'''
'''
'''
'''
######MATRICES

matriz=[[10,20],[20,30],[30,50],[60,70]]

print (matriz[1][1])

print (type(matriz))

##########
'''
########### DICCIONARIOS
'''
'''
'''
'''
alumno1 = {"nombre": "Pablo", "cursos": 3}

print (alumno1["nombre"])
print (alumno1["cursos"])
print (alumno1)
for clave in alumno1:
	print(clave)
	
print (list(alumno1.keys()))
print (list(alumno1.values()))
'''
'''
'''
###### funcion range
'''
'''

for i in range(1, 11):
	print(i)

for i in range(10, 21,2):
	print(i)

for i in range(10, 0,-1):
	print(i)
'''
###### COMPROBAR EL NUMERO isdecimal()

'''
'''
'''
edad = input("Ingrese edad: ")
print(type(edad))

print(edad.isdecimal())
print(edad.isdigit())
print(edad.isnumeric())
'''
'''

#El método isdecimal() que tienen los string nos va a
#permitir evaluar si “ese dato” ingresado es posible de convertir, o no.
#Tanto las funciones isdigit() como isnumeric() tienen el mismo proceso de trabajo y proporcionan la misma salida.
#La única diferencia entre los dos es que la función isdigit() devuelve el valor True sólo para los dígitos (0-9),
#mientras que la función isnumeric() devuelve True si contiene algún carácter numérico;
#podría ser otro idioma que se utilice en lugar de los dígitos originales 0-9.

##### para convertir usamos int()   float()  srt()  bool()

#### Funciones
'''
'''Las funciones nos permiten agrupar una o más líneas de código bajo
un mismo nombre. Su objetivo principal es el de evitar la repetición
de código, haciendo de un archivo de código de fuente más claro,
legible y fácil de mantener
'''
'''
n1= float(input("ingrese un numero: "))
n2= float(input("ingrese otro numero: "))

def operacion_matematica (numero1,numero2):
		suma = numero1+numero2
		return suma
		
print ("La suma es: ", operacion_matematica(n1,n2))
'''
'''
#### funcion con multiples valores de retorno


def minimo_y_maximo(lista):
	a=min(lista)
	b=max(lista)
	return [a,b]
	
listado_de_numeros = [1,2,3,4,5,6,7,8,9]
print(minimo_y_maximo(listado_de_numeros))
resultados = minimo_y_maximo(listado_de_numeros)
print("El mínimo es: ", resultados[0])
print("El máximo es: ", resultados[1])
'''
'''
'''
####### bibliotecas
'''
'''
'''Las bibliotecas contienen rutinas creadas que
proporcionan ayuda a los programadores. Es decir,
estas pasan a formar parte del código principal y por
lo tanto se escribe menos código ya que muchas
soluciones son posibles al incorporar las librerías,
esto permite un trabajo más modular y estándar. 
'''

#### importacion de la biblioteca a mi proyecto: import.....
#### diferentes bibliotecas nativas: random, os, math, sys, statistics......

####### APLICACIONES DE ESCRITORIO

### LIBRERIA TKINTER 

#### WIDGETS: VENTANA, BOTON, CAJA DE TEXTO, LABEL, BOTON DE OPCIONES, LISTA DE OPCIONES, ETC...

##import tkinter as tk
''''

'''

























		
		









	







