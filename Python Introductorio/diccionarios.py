#tupla = ("a","b","c")

#ver un valor de la tupla
#print (tupla[1])


#Demostracion de error al asignar un valor en la tupla  ------> no se reemplazan los valores en una tupla

#tupla[1]= "d"


#### DICCIONARIOS

temperaturas=[10,23,17,33]

diccionario = {123:"Carlos",456:"Jose",789:"Juan","temp":temperaturas}

# VER EL CONTENIDO DE UN DICCIONARIO

#print (diccionario[123])

#print (diccionario["temp"]) ##### las claves pueden ser cadenas o numeros

#print (diccionario["temp"][1])  ######## valor dentro de un valor que es una lista

#print(diccionario[123])     
print(diccionario.get(123)) 

# VER VALORES DE UN DICCIONARIO
#EJEMPLO CON VALUES()
d = {'1':'a','2':'b','3':'c','4':'d'}
print(d.values(),type(d.values()))
# EJEMPLO CON list ()  --->>> para pasar los valores a una lista

d = {'1':'a','2':'b','3':'c','4':'d'}
lst = list(d.values())
print(" Valores de la lista")
for valor in lst:
	print(valor)

#print(lst)

####  VER LAS CLAVES DE UN DICCIONARIO

#dicc =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
#keys= dicc.keys()
#print (keys)
#print (diccionario)



###### para agregar elementos no se usa ni append ni insert
##### no se pueden repetir las claves

diccionario[999]="Santa Fé"
#print (diccionario)

# Ejercicio AGREGAR UN ELEMENTO AL DICCIONARIO


#### recorrer un diccionario

for valor in diccionario:
	print (valor)
	
# Eliminar elementos de un diccionario ---> clean

dic ={"a":1,"b":2,"c":3 ,"d":4}
print(dic)
print("Borrramos el elemento b con del() ")
del dic["a"]
print(dic)
print ("borramos un elemento con pop()")
dic.pop("b","no se encuentra dato")
print(dic)
print(dic.pop("b","no se encuentra dato"))
print(dic.pop("b","no se encuentra dato"))
#del dic["b"] #----->>> da error porque el elemento no esta , pero en pop no dio error porque tiene un valor de respuesta por defecto.
#print(dic)
#print(dic.pop("b","no se encuentra dato"))




