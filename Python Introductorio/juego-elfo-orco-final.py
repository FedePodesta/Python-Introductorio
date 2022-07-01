hecho = False
vidasElfo=3
vidasOrco=3

while not hecho:
	salir = input ("Quiere salir?(s/n)")
	if salir =="s":
		hecho = True
	ataque = input ("atacar con el elfo (s/n)")
	if ataque == "s":
		#chequeo de ataque
		opcion= int(input("elija un numero entre 1 y 9"))
		if opcion == 1 or opcion ==3 or opcion ==5 or opcion ==7 or opcion ==9:
			
			vidasOrco = vidasOrco - 1
			# chequeo vidas orco
			if vidasOrco == 0:
				print ("el orco murió, HAS GANADO!!!")
				hecho = True
			else:
				print ("el orco está herido")
		else:
			print ("no le diste - ahora te atacan....")
			
	else:
		 hecho = True
		 
		
