n = int(input("Cuál es el número de pacientes? "))

suma_hombres = 0
suma_mujeres = 0
cont_hombres = 0
cont_mujeres = 0

for i in range(n):
    hemoglobina = float(input("Cuál es su nivel de hemoglobina?"))
    genero = int(input("Cuál es su género? (1=Masculino, 2=Femenino)"))
    while genero != 1 and genero != 2:
        genero = int(input("Cuál es su género? (1=Masculino, 2=Femenino)"))

    if genero == 1:
        suma_hombres += hemoglobina
        cont_hombres += 1
    else:
        suma_mujeres += hemoglobina
        cont_mujeres += 1

     #prom para los mentirosos 
if cont_hombres > 0:
    promedio_hombres = suma_hombres / cont_hombres
    if promedio_hombres < 12.2:
        alerta_hombres = "Baja"
    elif promedio_hombres <= 16.6:
        alerta_hombres = "Normal"
    else:
        alerta_hombres = "Alta"
else:
    promedio_hombres = 0.0
    alerta_hombres = "Sin datos"
 
     #prom para mujeres
if cont_mujeres > 0:
    promedio_mujeres = suma_mujeres / cont_mujeres
    if promedio_mujeres < 12.6:
        alerta_mujeres = "Baja"
    elif promedio_mujeres <= 15:
        alerta_mujeres = "Normal"
    else:
        alerta_mujeres = "Alta"
else:
    promedio_mujeres = 0.0
    alerta_mujeres = "Sin datos"


print(round(promedio_hombres, 2), alerta_hombres)
print(round(promedio_mujeres, 2), alerta_mujeres)

harriba=0
habajo=0 
higual=0
marriba=0
mabajo=0
migual=0

for i in range(n):
    hemoglobina = float(input("Cuál es su nivel de hemoglobina? "))
    genero = int(input("Cuál es su género? (1=Masculino, 2=Femenino) "))
    while genero != 1 and genero != 2:
        hemoglobina = float(input("Cuál es su nivel de hemoglobina? "))
        genero = int(input("Cuál es su género? (1=Masculino, 2=Femenino) "))

    if genero == 1:
        if hemoglobina > promedio_hombres:
            harriba += 1
        elif hemoglobina < promedio_hombres:
            habajo += 1
        else:
            higual += 1
    else:
        if hemoglobina > promedio_mujeres:
            marriba += 1
        elif hemoglobina < promedio_mujeres:
            mabajo += 1
        else:
            migual += 1

print(harriba, habajo)
print(marriba, mabajo)
print(higual, migual)
