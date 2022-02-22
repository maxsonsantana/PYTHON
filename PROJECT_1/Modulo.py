from Classes import Televisao
from AnonimousFunction import calculadora

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

print(type(calculadora))
soma = calculadora['soma']
subt = calculadora['sub']
print(soma(3, 7))
print(subt(5, 9))