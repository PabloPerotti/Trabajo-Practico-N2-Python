edad_uno = int(input("Ingrese la edad del primer usuario: "))
edad_dos = int(input("Ingrese la edad del segundo usuario: "))

if edad_uno >= edad_dos:
    diferencia = edad_uno - edad_dos
    print(f'la diferencia entre el usuario uno y el usuario dos es de : {diferencia} años')
else:
    diferencia = edad_dos - edad_uno
    print(f'la diferencia entre el usuario uno y el usuario dos es de : {diferencia} años')
    