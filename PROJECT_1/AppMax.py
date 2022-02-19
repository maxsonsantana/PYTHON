a = int(input('Entre com o 1º valor: '))
b = int(input('Entre com o 2º valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a/b
mod = a%b

#Concatena independente do tipo
print('soma: {} \n  Subtração: {}'.format(soma, subtracao))

#Converte tipo de dados de soma para Strint
soma = str(soma)

#Mostra o tipo da variável
print(type(soma))
print('soma: ' + str(soma))


