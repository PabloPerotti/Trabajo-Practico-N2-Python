precio_por_noche = float(input("Ingrese el precio por noche de alojamiento:"))
cantidad_dias = int(input("Ingrese la cantidad de Dias:"))

total_estadia = precio_por_noche * cantidad_dias
total_estadia_2dec = round(total_estadia, 2)

print(f"El total de la estadia es de {total_estadia_2dec} pesos.")
