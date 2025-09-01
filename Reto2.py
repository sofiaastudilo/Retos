n = int(input("Cuántos pacientes hay?"))

hombres_baja = 0
hombres_alta = 0
hombres_normal = 0
mujeres_baja = 0
mujeres_alta = 0
mujeres_normal = 0

for i in range(n):
    hemoglobina = float(input("Ingresa tu nivel de insulina"))
    genero = int(input("Ingresa tu genereo 1 para mascuino y 2 para femenino "))

    if genero == 1:  
        if hemoglobina < 12.2:
            print ("Está baja")
            hombres_baja += 1
        elif hemoglobina <= 16.6:
            print ("Está normal")
            hombres_normal += 1
        else:
            print ("Está alta")
            hombres_alta += 1

    elif genero == 2:  
        if hemoglobina < 12.6:
            print ("Está baja")
            mujeres_baja += 1
        elif hemoglobina <= 15:
            print ("Está normal")
            mujeres_normal += 1
        else:
            print ("Está alta")
            mujeres_alta += 1

print(hombres_baja, hombres_alta, hombres_normal,
      mujeres_baja, mujeres_alta, mujeres_normal)


