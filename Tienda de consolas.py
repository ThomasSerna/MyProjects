#           Notas
#Este Mini-Proyecto de python lo hice con el proposito de crear un ejemplo sobre una tiendo de consolas.

from colorama import Fore, init, Style
import MySimpleMath
import time

init()

while True:
    Objetos = ["-Xbox","-Play","-Switch"]
    ObjetosList = ["xbox","play","switch"]
    Finalizar = 0

    Presupuesto = input("Cuanto presupuesto tienes: ")
    print("\nNuestros productos:")

    for Objetos2 in Objetos:
        print(Objetos2)

    Mensaje1 = input("\nQue te gustaria comprar: ")

    if Mensaje1.lower() == ObjetosList[0]:
        Xbox = 2
        Finalizar = 1
        if int(Presupuesto) >= int(Xbox):
            Presupuesto2 = MySimpleMath.Resta(int(Presupuesto), int(Xbox))
            print(Fore.GREEN,f"\nFelicidades has obtenido tu {Mensaje1}")
            time.sleep(1)
            print(Style.RESET_ALL,f"\nTu actual presupuesto es de: {Presupuesto2}$")
            Finalizar = 1
        else:
            print(Fore.MAGENTA + "No tienes el suficiente presupuesto")

    elif Mensaje1.lower() == ObjetosList[1]:
        Play = 3
        Finalizar = 1
        if int(Presupuesto) >= int(Play):
            Presupuesto2 = MySimpleMath.Resta(int(Presupuesto), int(Play))
            print(Fore.BLUE,f"\nFelicidades has obtenido tu {Mensaje1}")
            time.sleep(1)
            print(Style.RESET_ALL,f"\nTu actual presupuesto es de: {Presupuesto2}$")
            Finalizar = 1
        else:
            print(Fore.MAGENTA + "No tienes el suficiente presupuesto")

    elif Mensaje1.lower() == ObjetosList[2]:
        Switch = 4
        Finalizar = 1
        if int(Presupuesto) >= int(Switch):
            Presupuesto2 = MySimpleMath.Resta(int(Presupuesto), int(Switch))
            print(Fore.LIGHTRED_EX,f"\nFelicidades has obtenido tu {Mensaje1}")
            time.sleep(1)
            print(Style.RESET_ALL,f"\nTu actual presupuesto es de: {Presupuesto2}$")
            Finalizar = 1
        else:
            print(Fore.MAGENTA + "No tienes el suficiente presupuesto")

    if Finalizar == 1:
        print(Fore.CYAN,Style.BRIGHT,"Gracias por visitarnos.\n  Vuelva pronto.")
    elif Finalizar == 0:
        print(Fore.RED,"Objeto incorrecto", Fore.RESET)
    Final = input("\n\nDesea cerrar el programa?:")
    if Final.title() == "Si":
            time.sleep(1)
            break
    if Final.title() == "No":
        time.sleep(1)
        print("Reiniciando programa")
        print("\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n",)
        print(Fore.LIGHTYELLOW_EX,"Programa reiniciado",Fore.RESET)
        continue        
    else:
        print(Fore.RED,"Respuesta incorrecta, usa Si/No",Fore.RESET)
        break