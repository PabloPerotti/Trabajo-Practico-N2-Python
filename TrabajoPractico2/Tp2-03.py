precio = float(input("Ingrese el precio del alojamiento por noche: ")) 
dias = int(input("Ingrese la cantidad de dias: "))
total = precio * dias
print("El precio total de la estadia es: {:.2f}".format(total))