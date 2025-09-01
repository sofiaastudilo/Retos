hemoglobina = float (input("Ingresa tu nivel de insulina"))
genero = float (input("Cuál es tu género? 1. (Para masculino) y 2. (Para femenino)"))

if genero == 1:
    if hemoglobina < 12.2:
       print ("Está baja")
    elif hemoglobina <= 16.6:
       print ("Está normal")
    else:
       print("Está alta")

elif genero == 2:
   if hemoglobina <12.6:
      print("Está baja")
   elif hemoglobina <=15:
      print("Está normal")
   else: 
      print ("Está alta")

else:
   print("No se puede generar la alerta")
