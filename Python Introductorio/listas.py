temperaturas = [15,20,16.5,23,25.8,31,30,"Carlos", True]
#print(temperaturas[-2])

#print(temperaturas)
#print (type(temperaturas))
#print (len(temperaturas))
#temperaturas[6]= 90
#print (temperaturas)
### ver elementos e una lista
#print (temperaturas)
#temperaturas[6]= 90
#print (temperaturas [6])
#print (type(temperaturas))

#### AGREGAR ELEMENTOS A UNA LISTA
### Insertar al final
#temperaturas.append(22222)
#temperaturas.append(["pepe","José"])
#print (temperaturas)
#print (temperaturas[-1])
#print (temperaturas[10][0])

#print (temperaturas[9])

### insertar segun el indice indicado

#print(temperaturas)
#listaprueba = ["carlos",10, True]
#temperaturas.insert (2,listaprueba)
#listaprueba.insert (8,"pepe")
#print (listaprueba)
#print (temperaturas)

'''
listaDeTemperaturas=[]

variable = float(input("ingrese una temperatura"))
listaDeTemperaturas.append(variable)
print(listaDeTemperaturas)

'''


#print (temperaturas)
#print ("La cantidad de elementos de la lista temperaturas es:",len(temperaturas))
#print (temperaturas [3])


### REMOVER UN ELEMENTO DE UNA LISTA

####borrar un elemento por su posicion
#print(temperaturas)
#print(temperaturas)
#del temperaturas [2]
#print (temperaturas)

##### Borrar el ultimo elemento de la lista
#temperaturas.pop()
#print(temperaturas)
##### Borrar un elemento segun su contenido

#nombres= ["Pepe","jose","Carlos","Juan","Pepe"]
#print(nombres)
#nombres.remove("Pepe")
#nombres.remove("Pepe")
#print(nombres)





#### cantidad de elementos de una lista
#print (len(temperaturas))
#### elegir el ultimo elemento de una lista
#print(temperaturas [6])
#numero_aleatorio= float(input("ingrese un numero"))
#print("can de elemntos que estan la lista",len(temperaturas))
#print ("resultado aleatorio", [len(temperaturas)-numero_aleatorio])

#### CREAR UNA LISTA VACIA
#temperaturas = []
#print (temperaturas)


#### RECORRER UNA LISTA

temperaturas = [15,20,16,23,15,31,30]

'''indice = 0
while indice < len(temperaturas):
	if indice == 0:
		print("El lunes la temp fue de: ",temperaturas[indice])
	indice = indice + 1
'''

''''''
#### ELIMINAR UN ELEMENTO DE LA LISTA SIN SABER EL INDICE
'''
##temperaturas.remove(15)
##temperaturas.remove(15)

'''
#print(temperaturas)

#### BORRAR EL VALOR DEL FINAL DE UNA LISTA
#temperaturas.pop()
#print(temperaturas)

#### ordenar una lista
'''
#temperaturas[2]="pepito"
'''
temperaturas.sort(desc)
#print (temperaturas)

#### valores maximos y minimos de una lista

print("La lista de temperaturas es: ", temperaturas)
print("El valor maximo de la lista es: ",max(temperaturas))
print("El valor minimo de la lista es: ",min(temperaturas))



