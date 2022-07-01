print ("******************************")
print ("HAGAMOS UNA OPERACIÓN")
print ("******************************")

print("1.Suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.division entera")
print("6.exponente")
print("7.modulo o resto \n")

numero= int(input("Introduce una opcion: "))

if numero ==1:
    print("Elegiste suma \n")
    numero =int (input("Introduce el primer numero: "))
    numero +=int(input("Introduce el segundo numero: "))
    print("el resultado de la suma es : ",numero)

elif numero ==2:
    print("Elegiste resta \n")
    numero =int (input("Introduce el primer numero: "))
    numero -=int(input("Introduce el segundo numero: "))
    print("el resultado de la resta es : ",numero)

elif numero ==3:
    print("Elegiste multiplicacion \n")
    numero =int (input("Introduce el primer numero: "))
    numero *=int(input("Introduce el segundo numero: "))
    print("el resultado de la Multiplicacion es : ",numero)

elif numero ==4:
    print("Elegiste division \n")
    numero =float (input("Introduce el primer numero: "))
    numero +=float (input("Introduce el segundo numero: "))
    print("el resultado de la division es : ",round(numero,2))

elif numero ==5:
    print("Elegiste Div. Entera \n")
    numero =int (input("Introduce el primer numero: "))
    numero //=int(input("Introduce el segundo numero: "))
    print("el resultado de la Div entera es : ",numero)

elif numero ==6:
    print("Elegiste Exponente \n")
    numero =int (input("Introduce el primer numero: "))
    numero **=int(input("Introduce el segundo numero: "))
    print("el resultado del Exponente es : ",numero)

elif numero ==7:
    print("Elegiste Modulo/resto \n")
    numero =int (input("Introduce el primer numero: "))
    numero %=int(input("Introduce el segundo numero: "))
    print("el resultado de la Modulo/resto es : ",numero)

else:
    print ("Opcion elegida no existe, vuelva a ejecutar el programa")
