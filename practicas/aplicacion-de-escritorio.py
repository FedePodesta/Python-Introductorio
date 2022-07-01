#APLICACION DE ESCRITORIO UTILIZANDO LA LIBRERIA TKINTER

import tkinter as tk

#### creamos la ventana ---- contenedora de todos los controles o widgets


#ventana = tk.Tk() ##### creo y ejecuto la ventana
#ventana.mainloop() ######## dejo abierta la ventana hasta que pase un evento, como por ejemplo hacer click en la cruz





####### configuracion de la ventana

ventana= tk.Tk()
ventana.config(width=800,height=600) #### ancho y alto en pixeles.
ventana.title("Bienvenido a la aplicacion")
#ventana.iconbitmap("icono1.ico") #Cambiar el icono
#ventana.config(bg="blue") #Cambiar color de fondo
#ventana.resizable(0,0)  	#no podras hacer la ventana más pequeña o más grande.
						#raiz.resizable(1,1) que es el que viene por defecto en tkinter,
						#para permitir la manipulacion del tamño de la venta por parte del usuario,
						#pero sin embargo; tkinter tambien permite establecer que el ancho pueda ser manipulado pero el alto no y viceversa.
						#Si quisiera que en la ventana de mi programa se pueda manipular solo el ancho usaria raiz.resizable(1,0)
						#y si quiero manipular solo el alto usaria raiz.resizable(0,1).
ventana.mainloop()



########### agregamos con boton en la ventana

#ventana1= tk.Tk()
#ventana1.config(width=500,height=400) #### ancho y alto en pixeles.
#ventana1.title("Bienvenido escritorio")



#def boton_presionado():
#	print("Hola mundo")
#	print(caja.get())


#boton = tk.Button(text="aceptar",command=boton_presionado)
#boton.place(x=20, y=50, width=150,height=50)
##ventana1.mainloop()

###función place(): las dos coordenadas de la posición y el ancho y el alto del tamaño.

############### agregamos una textbox y una etiqueta


#caja = tk.Entry()
#caja.place(x=20, y=100, width=100, height=25)  #### es análogo a input()
#etiqueta = tk.Label (text="Ingresa tu nombre",bg="#38C2EF",fg="#E00E0E")
#etiqueta.place(x=20, y=130)
##ventana1.mainloop()

def saludar():
	nombre = caja_saludo.get()
	etiqueta_saludo = tk.Label (bg="#ADD5E9")
	etiqueta_saludo.place(x=20, y=230)
	etiqueta_saludo.config(text="Hola " + nombre)

#caja_saludo = tk.Entry()
#caja_saludo.place(x=20, y=180, width=100, height=25)

#boton_saludo = tk.Button(text="Saludar",command=saludar)
#boton_saludo.place(x=20, y=250, width=100,height=40)

#ventana1.mainloop()


#### agregamos una etiqueta o label - indican informacion - son inmutables no se pueden editar


######## interaccion entre los controles


'''
def boton2_presionado():
	print("Hola mundo")

boton2 = tk.Button(text="Hola mundo", command=boton2_presionado)
boton2.place(x=20, y=150, width=100, height=30)

###### obtener el contenido de la caja de texto
##Todas las cajas de texto incluyen una función
##llamada get() que retorna la cadena
## (por más que el texto sea un número, al igual que input())
## ingresada por el usuario.



def boton_presionado():
	print(caja.get())

#########################

############ interaccion entre boton y label

def saludar():
	nombre = caja.get()
	etiqueta_saludo = tk.Label (bg="#ADD8E9")
	etiqueta_saludo.place(x=20, y=230)
	etiqueta_saludo.config(text="Hola" + nombre)
	
boton3 = tk.Button(text="Agregar", command=saludar)
boton3.place(x=20, y=200, width=100, height=30)




ventana1.mainloop()


'''


