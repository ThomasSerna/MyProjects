#           Notas
#Este proyecto esta echo de la finalidad de obtener el radio de un circulo, a traves de su diametro

Diamentro = float(input("Dame el diamentro de tu circulo: "))
Pi = 3.14159265359
Radio = Diamentro * Diamentro
Area = Radio * Pi
print(round(Area, 2))