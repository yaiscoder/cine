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

    print("¡Bienvenido/a!")
    print("Las sillas disponibles en el cine son las siguientes: ")
    for fila in cine:
       print(fila)
    opcion = input("¿Desea reservar una silla? yes/no: ")

    if opcion == "yes":
        f_asiento = int(input("¿Qué número de fila desea escoger? "))
        c_asiento = int(input("¿Qué número de asiento de esa fila desea?  "))

        cine[f_asiento - 1][c_asiento - 1] = "Taken"
           
    else: 
     break
