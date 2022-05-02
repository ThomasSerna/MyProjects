#           Notas
#Programa que promedia números

from time import sleep

S = 0

while True:
    CantidadPromediar = int(input('Dime cuantos número vas a promediar: '))
    if CantidadPromediar == 0:
        print('No puedes promediar 0 números')
    for i in range(1,CantidadPromediar+1):
        N = float(input(f'Dame el número {i}: '))
        S += N
    print(f'El promedio estos números es: {round(S/CantidadPromediar, 2)}')
    sleep(2.5)
    F = str(input('\nSi desea cerrar el programa escriba "salir": '))
    if 'salir' in F.lower():
        exit()