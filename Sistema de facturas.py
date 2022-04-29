#           Notas
#Sistema que genera facturas segun los datos de las variables.
from colorama import init,Fore
from time import sleep
from os import system
from os import name
from time import time
from datetime import datetime

init(autoreset=True)

if name in ('nt'):
    system('cls')

Vendedores = ['jose','ernesto','maria']
VendedoresID = [1,2,3]
ProductosStock = ['huevo','pan','cafe']
Clientes = []
LogFacturas = []

def Fecha():
    Fecha_ = datetime.today().strftime('%Y-%m-%d %H:%M')
    return Fecha_

def RestablecerColor():
    if name in ('nt'):
        system('color f')

while True:
    RestablecerColor()
    NombreVendedor = input('Cual es tu nombre: ')
    if NombreVendedor.lower() in Vendedores:
        IDVendedor = int(input('Cual es tu id de vendedor: '))
        if IDVendedor in VendedoresID:
            print(f'Bienvenido {NombreVendedor.capitalize()}')
            Tiempo1 = time()
            while True:
                RestablecerColor()
                Menu = str(input('\nQue desea hacer:\n1.Generar una factura\n2.Acceder al registro de anteriores facturas\n3.Acceder a datos del vendedor\n4.Cerrar programa\nElija una opcion: '))
                print('\n')
                if Menu in '1':
                    NombreCliente = str(input('Nombre del cliente: ')).lower()
                    if NombreCliente.lower() in Clientes:
                        pass
                    else:
                        print('Nuevo cliente; añadiendolo a la base de datos.')
                        Clientes.append(NombreCliente)
                        sleep(5)
                    ProductosFactura = []
                    while True:
                        RestablecerColor()
                        Producto = str(input('Ingrese el nombre del producto (En caso de finalizar la factura escriba "Finalizar"): '))
                        if Producto.lower() == 'finalizar':
                            FacturaFinal = f'''
                            Nombre del cliente: {NombreCliente.capitalize()}

                            Productos comprados: 
                            {ProductosFactura}

                            Fecha y hora actual: {Fecha()}
                            '''
                            print(FacturaFinal)
                            LogFacturas.append(FacturaFinal)
                            break
                        elif Producto.lower() in ProductosStock:
                            ProductosFactura.append(Producto.capitalize())
                            print(ProductosFactura)
                        else:
                            print('Producto no encontrado.')
                            sleep(0.5)
                elif Menu in '2':
                    print('Antiguas facturas:',end="\n")
                    for i in LogFacturas:
                        print(i)
                        print('----------')
                elif Menu in '3':
                    Tiempo2 = time()
                    TiempoActividad = Tiempo2-Tiempo1
                    print(f'Nombre del vendedor: {NombreVendedor.capitalize()}\nID del vendedor: {IDVendedor}\nTiempo de actividad: {round(TiempoActividad)} segundos.\nUltimos productos vendidos: {ProductosFactura}\nFacturas echas hoy: {len(LogFacturas)}\nFecha y hora actual: {Fecha()}')
                    sleep(5)
                    Menu3 = str(input('Presione enter para continuar'))
                    sleep(1.5)
                elif Menu in '4':
                    print('Cerrando programa')
                    sleep(1.5)
                    exit()
                else:
                    print(Fore.RED,'Escoja una opcion valida\n',Fore.RESET)
                    sleep(2.5)
        else:
            print(Fore.RED,'ID incorrecto.',Fore.RESET) 
            sleep(2.5)
            exit()
    else:
        print(Fore.RED,'Nombre no encontrado\n Si cree que se trata de un error comuniquese con los administradores.',Fore.RESET)
        sleep(2.5)
        exit()