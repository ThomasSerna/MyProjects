#           Notas
#Este script tiene la funcionalidad de servir como calculadora multifuncional

import time, os

if os.name in 'nt':
    os.system('cls')
else:
    try:
        os.system('clear')
    except:
        pass

while True:

    pi = 3.14159265359
    of = 0
    rf = None

    menu = str(input('Bienvenido a xThomsCalculator\n\nQue desea hacer:\n1.Sumar x números\n2.Restar x números\n3.Multiplicar x números\n4.Dividir x números\n5.Promediar x números\n6.Hallar area de figuras geometricas\n7.Intentar mi operación\n8.Cerrar xThomsCalculator\nEscoja alguna opción: '))

    if menu == '1' or menu.lower() == 'sumar':
        n = int(input('Cuantos números sumara: '))
        for i in range(1,n+1):
            nf = float(input(f'Dame el valor {i}: '))
            of += nf
        print(f'La suma de estos números es {round(of, 2)}')
    
    elif menu == '2' or menu.lower() == 'restar':
        n = int(input('Cuantos números restaras: '))
        for i in range(1, n+1):
            nf = float(input(f'Dame el valor {i}: '))
            if int(i) == 1: rf = nf
            else: rf = rf-nf
        print(f'La resta de estos números es {round(rf, 2)}')

    elif menu == '3' or menu.lower() == 'multiplicar':
        n1 = float(input('Dame el valor 1: '))
        n2 = float(input('Dame el valor 2: '))
        print(f'La multiplicación de estos números es {round(n1*n2, 2)}')

    elif menu == '4' or menu.lower() == 'dividir':
        n1 = float(input('Dame el dividendo: '))
        n2 = float(input('Dame el divisor: '))
        print(f'La división de estos números es {round(n1/n2, 2)}')
        if n1%n2 == 0: pass
        else: print(f'El residuo de esta division es {n1%n2}')

    elif menu == '5' or menu.lower() == 'promediar':
        CantidadPromediar = int(input('Dime cuantos números vas a promediar: '))
        if CantidadPromediar == 0:
            print('No puedes promediar 0 números')
        for i in range(1,CantidadPromediar+1):
            N = float(input(f'Dame el número {i}: '))
            of += N
        print(f'El promedio estos números es: {round(of/CantidadPromediar, 2)}')    

    elif menu == '6' or menu.lower() in 'area':

        menu2 = str(input('\n1.Sacar area a un cuadrado\n2.Sacar area a un rectangulo\n3.Sacar circunferencia a un circulo\n4.Sacar area a un triangulo equilatero\nEscoja una opción: '))

        if menu2 == '1' or menu2.lower() in 'cuadrado':
            a = float(input('Dame el lado 1: '))
            b = float(input('Dame el lado 2: '))
            print(f'El area de tu cuadrado es {a*b}')

        elif menu2 == '2' or menu2.lower() in 'rectangulo':
            a = float(input('Dame la base: '))
            b = float(input('Dame la altura: '))
            print(f'El area de tu rectangulo es {a*b}')

        elif menu2 == '3' or menu2.lower() in 'circulo':
            radio = float(input('Dame el radio de tu circulo: '))
            radio = radio*radio
            print(f'La circunferencia de tu circulo es {round(pi*radio, 2)}')

        elif menu2 == '4' or menu2.lower() in 'triangulo':
            base = float(input('Dame la base de tu triangulo: '))
            altura = float(input('Dame la altura de tu triangulo: '))
            sf = base*altura
            print(f'El area de tu triangulo equilatero es {round(sf/2, 2)}')

    elif menu == '7' or menu.lower() in 'operacion' or menu.lower() in 'operación':
        op = eval(input('Dame la operación a completar: '))
        print(f'El resultado de tu operación es {op}')

    elif menu == '8' or menu.lower() in 'salir':
        exit()

    else: print('Opcion incorrecta')
    
    print()
    time.sleep(5)