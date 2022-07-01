import tkinter as tk
 
######################################################

def convertir(dato):
	if dato.isdecimal():
		dato = int(dato)
	else:
		dato = "error"
	return dato

 
def sumar():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	a = convertir(a)
	b = cajados.get()
	b = convertir(b)
	if a !="error" and b !="error":
		c = a + b
	else:
		c = "error"
	cajatres.insert(0,c)
 
def restar():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	a = convertir(a)
	b = cajados.get()
	b = convertir(b)
	if a != "error" and b != "error":
		c = a - b
	else:
		c = "error"
	cajatres.insert(0,c)
 
def multiplicar():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	a = convertir(a)
	b = cajados.get()
	b = convertir(b)
	if a != "error" and b != "error":
		c = a * b
	else:
		c = "error"
	cajatres.insert(0,c)
 
def dividir():
	cajatres.delete(0,tk.END)
	a = cajauno.get()
	a = convertir(a)
	b = cajados.get()
	b = convertir(b)
	if a != "error" and b != "error" and b != 0:
	    c = a / b
	else:
		c = "error"
	cajatres.insert(0,c)
 
######################################################
 
ventana = tk.Tk()
ventana.config(width=300, height=300)
ventana.title("Calculadora")
 
etuno = tk.Label(text="Dato uno:")
etuno.place(x=20,y=30)

cajauno = tk.Entry()
cajauno.place(x=20,y=60,width=100)
 
 
etdos = tk.Label(text="Dato dos:")
etdos.place(x=180,y=30)

cajados = tk.Entry()
cajados.place(x=180,y=60,width=100)


bsuma = tk.Button(text=" + ",command=sumar)
bsuma.place(x=20, y =120)
 
brestar = tk.Button(text=" - ",command=restar)
brestar.place(x=100, y = 120)
 
bmult = tk.Button(text=" x ",command=multiplicar)
bmult.place(x=180, y = 120)
 
bdiv= tk.Button(text=" / ",command=dividir)
bdiv.place(x=260, y = 120)


ettres = tk.Label(text="Resultado:")
ettres.place(x=80,y=190)

cajatres = tk.Entry()
cajatres.place(x=80,y=220)


ventana.mainloop()
