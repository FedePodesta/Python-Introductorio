print ("******************************")
print ("Sistema vacacional de rappi")
print ("******************************")

nombre=input ("Ingrese su Nombre: ")
clave =int (input ("ingrese su clave: "))
antiguedad = float (input ("ingrese sus años trabajados: "))

if clave == 1 :
    if antiguedad == 1 and antiguedad < 2:
        print(nombre," tienes 6 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print(nombre, " tienes 14 dias de vacaciones")
    elif antiguedad >=7:
        print( nombre, " tienes 20 dias de vacaciones")
    else:
        print(nombre , " no tienes derecho a vacaciones")

elif clave == 2:
      if antiguedad == 1 and antiguedad < 2:
        print(nombre," tienes 7 dias de vacaciones")
      elif antiguedad >=2 and antiguedad <=6:
        print(nombre, " tienes 15 dias de vacaciones")
      elif antiguedad >=7:
        print( nombre, " tienes 22 dias de vacaciones")
      else:
        print(nombre , " no tienes derecho a vacaciones")

elif clave == 3:
         if antiguedad == 1 and antiguedad < 2:
             print(nombre," tienes 10 dias de vacaciones")
         elif antiguedad >=2 and antiguedad <=6:
             print(nombre, " tienes 20 dias de vacaciones")
         elif antiguedad >=7:
              print( nombre, " tienes 30 dias de vacaciones")
         else:
             print(nombre , " no tienes derecho a vacaciones")    
             
else:
    print("La clave no existe")
    print ("fin")


