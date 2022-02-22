contador_letras = lambda lista: [len(i) for i in lista]
lista_animais = ['Cachorro', 'macaco', 'rinocerante']
print (contador_letras(lista_animais))

soma = lambda a, b: a + b
print ('Resultado da soma: {}'.format(soma(5, 7)))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subt = calculadora['sub']
print(soma(3, 7))
print(subt(5, 9))