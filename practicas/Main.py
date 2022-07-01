'''
print ("Hola Mundo")
print (2+2)
print ("curso de python")

#print ("edad; ", 10+10)
#print (2/0)
pepe = 2+2 #suma de 2 mas dos
print ("El resultado de la suma de 2+2 es: " , pepe)
jose = pepe + pepe
Lunes = 17
Martes = 16
Miercoles = 12
Jueves = 10.5
Viernes = 14
promedio = (Lunes+Martes+Miercoles+Jueves+Viernes)/5
print ("El promedio de temperatura es ", promedio)
print (jose*3)
print ("hola")
pedro=10**2
jose =10//3
carlos = 10%3
print (pedro)
print(jose)
print (carlos)

pepe=10
jose=10
fulano=8
print (jose==pepe)# dara false ya que no es igual
print (jose==fulano)#dara false ya que no es igual

entero = 10
flotante = 10.5
stringOcaracteres = "carlos" #siempre comillas
booleano = True # o tambien False(siempre mayuscula)

print (type(entero))
print (type(flotante))
print (type(stringOcaracteres))
print (type(booleano))

entero = "carlos"
print(type(entero))

temp_lunes =21
temp_martes = 30
temp_miercoles= 12
 #LAS VARIABLES TIENEN QUE SER LO MAS DESCRIPTIVO POSIBLE

Problema1 = 8!=1
Problema2=4<6
Problema3 = 16<=4
print (type (Problema1),Problema1)
print (type (Problema2),Problema2)
print (type (Problema3),Problema3)
#o sino
print (type(15==20),15==20)


# EJERCICIOS DEL MATERIAL DE ESUDIO
print ("Ejercicio Desafio 1")

texto1="el sol "
texto2="es muy "
texto3="caliente"
Frase=(texto1+texto2+texto3)
print (Frase)

print ("Ejercicio Desafio 2")

base = 10
altura = 5 
print ("el area del rectangulo es",base*altura)

print ("Ejercicio Desafio 3")
a=20
b=10
print ("A es igual a 20 B es igual a 10 entonces:")
print ("la suma de los valores es ",a+b)
print ("la resta de los valores es ",a-b)
print ("la division de los valores es ",a/b)
print ("la multiplicacion de los valores es ",a*b)

print:("desafio 2, ejercicio 1")
nota_uno= 10
nota_dos = 6
nota_tres = 8
promedio = (nota_uno+nota_dos+nota_tres)/3
print ("el promedio de las notas es ", promedio)

print("desafio 2, ejercicio 2")
edad = 15
if edad >= 18:
	print ("La persona es Mayor de Edad")
else: 
	print (" La persona es Menor de edad")

print ("Desafio 2, ejercicio 3")

sueldo_total=300*6 + 500*4 + 700*2
sueldo_promedio= sueldo_total /12

print ("El sueldo promedio es: ", sueldo_promedio)

if sueldo_promedio < 300:
	print ("El sueldo es bajo")
elif sueldo_promedio < 900:
	print ("El sueldo es Normal")
else:
	print ("El sueldo es mejor de lo normal")
# EJERCICIOS DEL MATERIAL DE ESUDIO	



a=10
b=20
c=30
print (a<b and c>a) #dara true ya que las dos operaciones son Correctas		
					#si uno de los dos es falso devolverá false ya que 
					#las dos tienen que serlo
print (a<b or c<a) # dara true con que uno sea verdadero ya devolverá T				

print(not(a<b and c<a and c<b) #dara true ya que el NOT anula lo anterior

#Estructuras en la programación.

a=10
b=20
c=30
if a < b:
	print("hola mundo")


if a < b and c > a:
	print ("hola mundo")#se imprime ya que las dos condiciones son true

if a>b or a==c:     
	print("hola mundo33") # no se imprime ya que ninguna es true
						# si una de las dos es True (en "or", se imprim)


a=10
b=20
c=30	
			
if a>b:
	print("esto es asi")
else:
	print("es de otra forma") #se imprimé esto ya que la cond es false
	
if b!=a and c > a:
	print ("vamos por buen camino") # se impre esto ya cond es true
else:
	print ("dedicate a otra cosa")
	

temperatura= 28

if temperatura > 10:
	print("hace calor")
else:
	print ("hace frio")

temperatura = 8
humedad = 40

if temperatura >20 and temperatura< 30:
	print ("hace calor")
	if humedad == 90:
		print("ademas llueve")
	else:
		print("milagro no llueve")
elif temperatura >=10 and temperatura < 20:
	print ("templado")
elif temperatura > 30 and temperatura < 40:
	print ("es un infierno")
elif temperatura < 1:
	print ("Congelado")
elif temperatura >=2 and temperatura < 10:
	print("hace frio")
	if humedad <= 50:
		print("humedad normal")
	else:
		 print ("Solo hace frio")
else:
	print ("hace frio")

usuario="Pepe"
passw="1234"
if usuario == "Pepe" and passw=="1234":
		print("OK")
elif usuario == "Pepe" and passw!="1234":#podria haber puesto solo passw!="1234"
		print("Contraseña incorrecta, acceso denegado")
elif usuario != "Pepe" and passw=="1234":#podria haber puesto solo usuario!="Pepe"
		print("Usuario incorrecto, acceso denegado")
else:
	 print ("usuario y contraseña incorrecta")	

a=input ("ingrese un numero: ")
b=input ("otro numero: ")
print (a+b) # pero no los va a transformar a entero, salen concatenados
#entonces

a=int(input ("ingrese un numero: "))#puede ser  int, float
b=int (input("ingrese otro numero: "))
print(a+b)
	

temperatura = int(input("ingrese temperatura: "))
humedad = int(input ("ingrese humedad: "))

if temperatura >20 and temperatura< 30:
	print ("hace calor")
	if humedad == 90:
		print("ademas llueve")
	else:
		print("milagro no llueve")
elif temperatura >=10 and temperatura < 20:
	print ("templado")
elif temperatura > 30 and temperatura < 40:
	print ("es un infierno")
elif temperatura < 1:
	print ("Congelado")
elif temperatura >=2 and temperatura < 10:
	print("hace frio")
	if humedad <= 50:
		print("humedad normal")
	else:
		 print ("Solo hace frio")
else:
	print ("hace frio")		



		
usuario= input("ingrese nombre de usuario: ")# Todo lo que toma el teclado es = a un string no hace falta aclarar
passw= (input("ingrese Contraseña: "))		#salvo que sea un int,float.

if usuario == "Pepe" and passw=="1234":
		print("OK")
elif usuario == "Pepe" and passw!="1234": #podria haber puesto solo passw!="1234"
		print("Contraseña incorrecta, acceso denegado")
elif usuario != "Pepe" and passw=="1234": #podria haber puesto solo usuario!="Pepe"
		print("Usuario incorrecto, acceso denegado")
else:
	 print ("usuario y contraseña incorrecta")	

a=1
while True:
	if a < 5:
		print ("hola mundo")
		a = a+1
	else:
		print("mayor a 5" )
		break

while True:
	salir = input ("quieres salir? s/n")
	if salir =="s":
		break
	ataque = input ("atacar con el elfo (s/n): ")
	if ataque =="s":
		print( "has fallado")
	else:
		print("el orco te quito 1 hp, hp= 2")
	ataque = input("atacar al orco= s/n: ")
	if ataque =="s":
		print( " has fallado, el orco contra ataca, hp=1")
		ataqueEspecial= input("el orco bajo la guardia, atacar?(s/n) :")
	if ataqueEspecial =="s":
		print("tu ataque especial ha quitado 3 puntos de vida, has ganado")
		lot = input("Encontraste un cofre , quieres abrirlo o te marchas:(irme/abrirlo): ")
	if lot == "abrirlo":
		print ("El Cofre tenia un hechizo explosivo, mueres.")
	elif lot== "irme":
		print("regresas a tu ciudad triunfante , has ganado")
			
		break

while True:
	ingresar = input ("Mientras Exploras encuentras un dungeon: entrar o irse: ")
	if ingresar == "entrar":
		print(" Entras al Dungeon")
	else:
			print (" mientras te marchas ,te tropiezas y mueres, cobarde, GAME OVER")	
			break		
	ataque = input ("Un orco te desafia,como atacas? espada, hechizo fuego(fuego),lanzar piedra(piedra) :")
	if ataque== "espada":
		print ("el orco pierde 1 punto de vida (2/3) su contra ataque te mata, GAME OVER")
	elif ataque == "fuego":
		print("el orco se incendia tu ataque quita 3 puntos de vida (0/3) TU GANAS")
	elif ataque == "piedra":
		print ("el orco agarra la piedra y te la vuelve a lanzar, mueres , GAME OVER")
		break		

total=0
contar=0

temperatura = float (input("introduzca una temperatura mayor a 0"))

while temperatura > 0:
	total=total+temperatura
	contar = contar+1
	temperatura = float (input ("introduzca temperatura"))
	print ("el subproemedio de temperatura es : ", total/contar)
print ("el proemedio de temperatura es : ", total/contar)
	
	
lista= [1,"4",7,0]

print(lista[0]) #se puede usar  -3 los lugares siempre arrancan en 0 
#en este caso el 1 es pos 0 el "4" es pos 1 el 7 es pos 2 y el 0 pos 3


lista= [1,"4444",7,0,9]
print (lista[3])


temperaturas = [15,20,16.5,23,25.8,31,30,"Carlos",True]
print (temperaturas[7]) # imprime "carlos que esta en la 7ma pos tambien -2
print (type(temperaturas)) #dara tipo list, ya que es una lista
print (len(temperaturas)) #cuenta la cantidad de elementos en la lista 8

#ver elementos en una lista
temperaturas [6]=90 # cambia el valor de la posicion 6 de la lista
print (temperaturas)

#agregar elementos a la lista
temperaturas.append (2222) #agrega al final de la lista el valor
temperaturas.append (["pepe","jose"])# agregamos otra lista a otra lista
print (temperaturas)
print (temperaturas[9])
print (temperaturas[10])
print (temperaturas[10][0])

temperaturas = [15,20,16.5,23,25.8,31,30,"Carlos",True]
listaprueba=["carlos",False,4]
temperaturas.insert(2,listaprueba)
print (temperaturas)

listaTemperatura = []
temperaturas =float(input("ingrese una temperatura: "))
listaTemperatura.append(temperaturas)
print (listaTemperatura)

while listaTemperatura =<8:
	
#generacion de  7 temp
temperaturas=[]
contador=1
suma=0

while contador <=8:
	numero=float(input("ingrese la temperatura: "))
	temperaturas.append(numero)
	contador+=1
	suma+=numero
	promedio=suma/len(temperaturas)
	print(promedio)

print("Lista de temperaturas", temperaturas)
print("El promedio de temperaturas es",promedio)
print(len(temperaturas))
		
#REMOVER UN ELEMENTO DE LA LISTA
lista = [2,4,6,1,"asd"]
print (lista)
del lista[2]
print(lista)

#borrar el ultimo elemento de la lista
lista.pop()
print (lista)


Lista = [2,5,6,1,3,2,7]
valores = int(input ("cuantos elementos quiere borrar: "))
contador = 0
while valores >= contador:
	Lista.pop()
	contador= contador + 1
	print(Lista)


nombres = ["pepe","jose","carlos","pepe"]
print(nombres)
nombres.remove("pepe")
print(nombres)
'''
#temperaturas = [15,21,32,42,42,41,61]
#dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#indice=0
#while indice < len(temperaturas):
#	print ("La temperatura del " , dias[indice] , "fue de : " , temperaturas [indice] , " grados.")
#	indice += 1
#temperaturas= [12,23,62,12,72,12,61]
#temperaturas.sort()
#
#print ("La lista de temperatura es: ", temperaturas)
#print ("el Valor maximo de la lista es : ",max(temperaturas))
#print ( " El valor minimo de la lista es:", min (temperaturas))	
#temperaturas = [15,20,25]
#prov = []
#indice=0
#
#while indice <=3:
#	prov.append (input("Escriba una provincia: "))
#	indice= indice+1
#print("selecciono las siguientes provincias:")
#for i in prov:
#	print (i)

#nombres= ["pablo","jorge","pedro"]
#cant_alumnos= 0
#for i in nombres:
#	print("elnombre del alimno es: ",i)
#	cant_alumnos= cant_alumnos + 1
#print("la cant de alimnos es: ", cant_alumnos)
	
#temperaturas = [15,23,54,12,31]
#print ("las temperaturas de la semana fueron: ")
#for i in temperaturas:
#	print (i)
#print("el promedio semanal es: ",(i/3))


#for i in "Python": #string aparecen una letra de por vez
#	print (i)

#cant=0
#cadena=input("ingrese una cadena: ")
#for i in cadena:
#	cant+=1
#print ("cantidad de letras :",cant)

#for i in "python":# el continue saltea una vuelta , el break frena
#	if i =="y":
#		continue #o break
#	else:
#		print(i)

#for elemento in [1,2,3]:
#	print (elemento)
#	
#for elemento in (1,2,3):
#	print (elemento)
#	
#for key in {'one:1','two:2'}:
#	print (key)
#
#for char in "123":
#	print (char)

#contador=1	
#for line in open ("myfile.txt"):
#	print(line)
#	contador= contador+1
#print ("la cantidad de ciclados fue: ",contador)

#matriz = [["mendoza",15],["san juan",20],["san luis",10]]
#
#for x in matriz:
#	print("la provincia es " , x[0], "y la temperatura es: ",x[1])
	
#matriz = [[3.3,6.1,4.0],[4.9,32,4.1]]
#print (matriz)
#fila = int(input ("Fila: "))
#columna = int (input("Columna: "))
#if fila < len(matriz):
#	if columna < len (matriz[fila]):
#		print (matriz[fila][columna])
#	else:
#		print("error")

#def imprimir_saludo():
#	print("hola loco")
#	print("jeje")

#print("hola")
#print ("desde python")

# a=5 
# b=7
# print(a+b)

# imprimir_saludo()

# while a < b:
# 	print("todavia es bajo")
# 	a = a + 1
# 	if a >= b:
# 		print ("ahora si")

#Función para forzar el ingreso numérico.
#Crear una función que fuerce el ingreso de solo
#números. Debe recibir un número por argumento,
#y verificar que este sea un número posible de
#convertir a INT. En caso contrario, volver a pedir
#el ingreso dentro de la función. Deber de retornar
#el valor convertido a INT.

#def convertir(valor):
#    while valor.isdecimal() ==  False:
#        print("Error")
#        valor = input("Ingrese nuevamente: ")
#        valor = int(valor)
#        print ("exito")
#    return valor
# 
#convertir("1")	
#   


#Realiza una función llamada “area_rectangulo”
#que reciba la base y la altura por argumento y
#que devuelva (retorne) el área dell rectángulo.	

#def area_rectangulo (base,altura):
#	area =base * altura
#	return area
#
#print(area_rectangulo(10,5))
	



#Crea una función que reciba un dato ingresado
#por teclado (string), que verifique que sea un
#número entero posible de convertir (a entero),
#y si no lo es vuelva a pedir ese dato, hasta
#que sea posible de convertirlo. Luego, que
#retorne el entero convertido.

#def convertir(valor):
#	while valor.isdecimal()== False:
#		print ("Ingrese solo numeros enteros")
#		valor= input ("ingrese un numero entero: ")
#	valor = int(valor)
#	print ("exito")
#	return valor
#	
#convertir("asd")



#def rango(desde, hasta, intervalo):
#    numeros = []
#    while desde < hasta:
#        numeros.append(desde)
#        desde = desde + intervalo
#    return numeros
#
#
#lista = rango(1, 10, 2)
#print(lista)
#

#temperaturas = [10,23,11,22]

#diccionario ={123:"carlos",456:"jose",321:"322","temp":temperaturas}

#print (diccionario ["temp"][2])

''' Buen Ejercicio tiene todo
		
inicio = int (input (" ingrese el numero inicial: "))
final = int (input("ingrese el numero final: "))

multiplos5 = []
multiplos3 = []
multiplosnada = []

for n in range(inicio, final+1):
	if n%3 == 0:
		multiplos3.append (n)
	elif n%5 == 0:
		multiplos5.append (n)
	else:
		multiplosnada.append(n)

print ("multiplos de 3: ", multiplos3)
print ("multiplos de 5: ", multiplos5)
print ("No son multiplos: ", multiplosnada)		


ganador =4

def play():
	valores =[1,2,3,4,5]
	contador=1
	while contador <4:
		sel = int(input("ingrese un valor del 1 al 5: "))
		if sel !=ganador:
			contador +=1
			print("MAL ,Te quedan ", 4 - contador)	
		else:
			print("GANASTE ERA 4")
			break
			 
		

			
		
play()



from operator import truediv


def suma(a,b):
    print("Resultado=",a+b)

def resta(a,b):
    print("Resultado resta=",a-b)

def multiplicacion(a,b):
    print("Resultado multiplicacion",a*b)

def division(a,b):
    print("Resultado division",a/b)

def carga_datos():
    print("Opciones: 1 + // 2 - // 3 * // 4 /")
    opcion=input("Ingrese la opcion que quiere realizar: ")
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    if opcion =="1":
        suma(num1, num2)
    elif opcion=="2":
        resta(num1,num2)
    elif opcion=="3":
        multiplicacion(num1, num2)
    else:
        division(num1, num2)
carga_datos()

while True:
	pregunta=input("Quiere seguir haciendo calculos? (s/n) ")
	if pregunta == "s":
		carga_datos()
	elif pregunta == "n":
		print("Gracias por usar el sistema")
		break

	
def volCilindro (radio,altura):
	pi= 3.14
	resultado=pi*(radio**2)*altura
	print("El resultado es: ",resultado)

r=int(input("ingrese el radio: "))
alt=int(input("ingresela altura: "))

volCilindro(r,alt)

import time

i = 0

while i <11:
	print(i)
	time.sleep(1)
	i=i+1
print("La fecha de hoy es: ", time.asctime())

	

import time

while True:
	time.sleep(2)
	print("verde")
	time.sleep(2)
	print("amarillo")
	time.sleep(2)
	print("rojo")

import random

print("numero aleatorio", random.randrange(100))


import random
while True:
	print("menu")
	print ("1 - tirar dado")
	print ("2-salir")
	opcion = int(input(">>"))
	if opcion ==1:
		valor = random.randint(1,6)
		print("el valor del dado es : ",valor)
	elif opcion ==2:
		print("adios")
		break

import random
opciones=["piedra","papel","tijera"]
opcionaleatoria= random.randrange(3)
print (opcionaleatoria)
print("la opcion elejida es: ",opciones[opcionaleatoria])

'''

import random
regalos=["tv","tostadora","poncho","horno","cama","batidora"]

for sorteo in range(1):
	regalo=regalos[random.randint(0,6)]
	print("sorteo",sorteo+1,":",regalo)

random.shuffle(regalos) # metodo para mezclar la ubicacion de los elementos de una lista
print(regalos)
random.shuffle(regalos)
print(regalos)
	

	


	




	

 















