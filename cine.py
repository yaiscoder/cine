filas = 8
columnas = 10
cine = []
opcion = "yes"

def ImprimirTabla():
    for i in range(filas):
        fila = []
        for o in range(columnas):
            fila.append("Free")
        cine.append(fila)

print("-"*20)
print("¡Bienvenido/a")
print("-"*20)
ImprimirTabla()

while opcion == "yes":
    print("-"*50)
    print("Las sillas disponibles en el cine son las siguientes: ")
    print("-"*80)
    for fila in cine:
       print(fila)
    print("-"*80)
    opcion = input("¿Desea reservar una silla? yes/no: ")
    print("-"*50)

    if opcion == "yes":
        f_asiento = int(input("¿Qué número de fila desea escoger? "))
        print("-"*50)
        c_asiento = int(input("¿Qué número de asiento de esa fila desea?  "))

        if 0 == f_asiento or f_asiento > 8 or 0 == c_asiento or c_asiento > 10:
            print("-"*70)
            print("¡Recuerda que las filas van en un rango de (1-8) y las columnas de (1-10)!")
            print("-"*70)
            
        elif cine[f_asiento - 1][c_asiento-1] == "Taken":
            print("-"*80)
            print("Este asiento ya está ocupado, por favor , escoja otro: ")
            print("-"*80)
        elif cine[f_asiento - 1][c_asiento-1] == "Free":
            cine[f_asiento - 1][c_asiento - 1] = "Taken"
    else:
        break
