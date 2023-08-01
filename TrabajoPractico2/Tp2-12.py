año = 2023
edad = int(input("Ingrese su edad: "))
if edad >= 1000:
    print("la edad tiene que ser menor o igual que 1000")
    edad = int(input("Ingrese la edad correctamente: "))
    cumple = (año - edad)+1000
    print(f"en el año {cumple} cumpliria 1000 años") 
else:
    cumple = (año - edad)+1000
    print(f"en el año {cumple} cumpliria 1000 años") 