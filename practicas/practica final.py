import tkinter as tk

#ventana = tk.Tk() ### creo y ejecuto la ventana
#ventana.mainloop()###dejo abierta la ventana hasta que pase un evento como por ej hacer lick en la cruz


###config de la ventana

#ventana=tk.Tk()
#ventana.config(width=800,height=600)###ancho y alto de pixeles
#ventana.title =("Bienvenido a la aplicacion")
#ventana.iconbitmap("asd.ico")#cambiar el icono
#ventana.config(bg="blue")#cambia el color de fondo
#ventana.resizable(0,0) # no se puede modificar el temaño de la ventana
                        #raiz.resizable(1,1) es el por defecto
 # ventana.mainloop() 

def boton_presionado():
    print("hola mundo")

ventana1=tk.Tk()
ventana1.config(width=500,height=400)###ancho y alto de pixeles
ventana1.title =("Bienvenido a la aplicacion")
boton =tk.Button(text="Aceptar", command=boton_presionado)
boton.place (x=20,y=150,width=150, height=50)

caja=tk.Entry()
caja.place (x=20, y=100,width=200, height=25) ### es analogo a input()
etiqueta = tk.Label (text= "ingresa tu nombre",bg="#39c2ef",fg="#1a1a1a")
etiqueta.place(x=320,y=100)

#ventana1.mainloop()

def saludar():
    nombre = caja_saludo.get()
    etiqueta_saludo =tk.Label (bg="#add5e9")
    etiqueta_saludo.place(x=20, y=230)
    etiqueta_saludo.config(text="hola"+ nombre)

caja_saludo =tk.Entry()
caja_saludo.place(x=20, y=180,width=100,height=25)

boton_saludo = tk.Button(text="saludar",command=saludar)
boton_saludo.place(x=20,y=250,width=100,height=40)


ventana1.mainloop()
















