# class elemao:
#     def __init__(self):
#         print("Hola Mundo")
#     def mensaje(self):
#         print("Adios Mundo")
#     def mensaje2(self):
#         print("Webos")
# m = elemao
# #m.mensaje()
# #m.mensaje2()
# m.mensaje2()
# class fotopadre:
#     def __init__(self, numero):
#         self.numero = numero
#     def m1(self):
#         print("m1")
#     def m2(self):
#         print("m2")
#     def m3(self):
#         print("m3")
# class fotohijo(fotopadre):
#     def __init__(self, numero):
#         super().__init__(numero)
#     def m4(self):
#         print("m4")
#         print(self.numero + 10)
#     def m5(self):
#         print("m5")
#     def m6(self):
#         print("m6")

# ff = fotohijo(2)
# ff.m4()

class so:
    def __init__(self):
        self.numero = 0
    def operacion(self):
        a = self.numero + 20
        print(a)
    def resultado(self):
        return self.numero
ex = so()
ex.operacion()