class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print('Canal: {}'.format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}'.format(televisao.canal))



# class Calculator:
#     def __init__(self):
#         pass
#
#     def soma(self, a, b):
#         return a + b
#
#     def subt(self, a, b):
#         return a - b
#
#     def div(self, a, b):
#         return a / b
#
#     def mult(self, a, b):
#         return a * b
#
# calculadora = Calculator()
# print('Soma: {}'.format(calculadora.soma(3, 5)))
# print('Subtração {}'.format(calculadora.subt(3, 9)))
# print('Divisao {}'.format(calculadora.div(14, 5)))
# print('Multiplicação {}'.format(calculadora.mult(3, 7)))


# class Calculator:
#     def __init__(self, num1, num2):
#         self.a = num1
#         self.b = num2
#
#     def soma(self):
#         return self.a + self.b
#
#     def subt(self):
#         return self.a  - self.b
#
#     def div(self):
#         return self.a / self.b
#
#     def mult(self):
#         return self.a * self.b
#
# calculadora = Calculator(10, 2)
# print(calculadora.a)
# print(calculadora.b)
# print('Soma: {}'.format(calculadora.soma()))
# print('Subtração {}'.format(calculadora.subt()))
# print('Divisao {}'.format(calculadora.div()))
# print('Multiplicação {}'.format(calculadora.mult()))
