filas = 8
columnas = 10
cine = []
opcion = "yes"

for i in range(filas):
    fila = []
    for o in range(columnas):
        fila.append("Free")
    cine.append(fila)

while opcion == "yes":
    print("*"*20)
    print("¡Bienvenido/a")
    print("*"*20)
    print("Las sillas disponibles en el cine son las siguientes: ")
    print("*"*80)
    for fila in cine:
       print(fila)
    print("*"*80)
    opcion = input("¿Desea reservar una silla? yes/no: ")

    if opcion == "yes":
        f_asiento = int(input("¿Qué número de fila desea escoger? "))
        c_asiento = int(input("¿Qué número de asiento de esa fila desea?  "))

        if cine[f_asiento - 1][c_asiento - 1] == "Taken":
           print("*"*80)
           print("Este asiento ya está ocupado, por favor , resever otro: ")
           print("*"*80)
           f_asiento = int(input("¿Qué número de fila desea escoger? "))
           c_asiento = int(input("¿Qué número de asiento de esa fila desea?  "))

     
        cine[f_asiento - 1][c_asiento - 1] = "Taken"
           
    else: 
     break
