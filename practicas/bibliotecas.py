####### BIBLIOTECAS
'''
Llamada ---> librería es un conjunto de implementaciones funcionales,
codificadas en un lenguaje de programación
Contienen rutinas creadas que proporcionan ayuda a los programadores.
Pasan a formar parte del código principal y por lo tanto se escribe menos código
ya que muchas soluciones son posibles al incorporar las librerías, esto permite un trabajo más
modular y estándar. 
'''
#Biblioteca standart ---->>> https://docs.python.org/es/3/library/index.html




##### BIBLIOTECA INCORPORADAS

#### TIME

import time

'''
i = 0

while i < 10:
    print(i)
    time.sleep(2)
    i = i + 1

print("La fecha de hoy es: ", time.asctime())

while True:
	print("s
'''


'''

##### RANDRANGE  ---->>> Construye numeros aleatorios

'''

import random

####EJEMPLO 1

#print ("Numero aleatorio dentro de un rango", random.randrange(100))

####EJEMPLO 2

#print ("Numero aleatorio dentro de un rango", random.randrange(60,100))

'''



####EJEMPLO 3 --------- dados!!!!
'''
'''
import random
while True:
    print("Menú")
    print("1 - Tirar dado")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        valor = random.randint(1,6)
        print("El valor del dado es:", valor)
    elif opcion == "2":
        print(" ¡Gracias por usar nuestro programa! ")
        break
    else:
        print("¡No existe esa opción!")
'''
'''

'''
##### Piedra - Papel - Tijera
import random
'''opciones=["piedra","papel","tijera"]
opcion_aleatoria= random.randrange(3)
print (opcion_aleatoria)
print("la opcion elejida es: ", opciones[opcion_aleatoria])



'''
######## Sorteo

regalos=["TV","RADIO","LICUADORA","AUTO","BICI","SEGUI PARTICIPADO"]

print (regalos)
#for sorteo in range(6):
#	regalo=regalos[random.randint(0,5)]
#	print("Sorteo", sorteo+1, ": ",regalo)

random.shuffle(regalos) # método para mezclar la ubicacion de los elementos de una lista
print (regalos)
random.shuffle(regalos)
print (regalos)








