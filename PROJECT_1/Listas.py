lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print('Lista Original: {}'.format(lista_animal))
lista_animal.append('macaco')
print('append: {}'.format(lista_animal))
lista_animal.pop()
print('pop(): {}'.format(lista_animal))
lista_animal.pop(1)
print('pop(1): {}'.format(lista_animal))
lista_animal.remove('cachorro')
print('remove cachorro: {}'.format(lista_animal))
lista_animal.append(['macaco', 'girafa', 'Rinocerante', 'Onça'])
print('Nova lista: {}'.format(lista_animal))
# lista_animal.sort()
# print('Lista Ordenada: {}'.format(lista_animal))
lista.sort()
print(lista)
lista.reverse()
print(lista)
tupla = (1, 3, 7, 90)
print(tupla)
print(len(lista_animal))
listat = tuple(lista)
print(listat)
#list : Converte para lista(vetor)
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('nao existe um gato na lista')

#print(lista_animal[1])
# print(min(lista))
#
# for x in lista_animal:
#     print(x)