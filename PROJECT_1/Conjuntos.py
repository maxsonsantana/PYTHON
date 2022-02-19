conjunto = {1, 2, 3, 4, 5, 6}
conjunto2 = {5, 6, 7, 8, 9}
conjunto_uniao = conjunto.union(conjunto2)
conjunto_intersecao = conjunto.intersection(conjunto2)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
lista = ['gato', 'cachorro', 'macaco', 'gato', 'papagaio']
conjunto_lista = set(lista)
print('Conjunto 1: {}'.format(conjunto))
print('Conjunto 2: {}'.format(conjunto2))
print('União: {}'.format(conjunto_uniao))
print('Interseção: {}'.format(conjunto_intersecao))
print('Direrença: {}'.format(conjunto_diferenca))
print('Direrença Simétrica: {}'.format(conjunto_diff_simetrica))
print('Lista: {}'.format(lista))
print('Lista Convertida: {}'.format(conjunto_lista))




# conjunto = {1, 1, 2, 3, 4, 3, 2}
# print(type(conjunto))
# print(conjunto)
# conjunto.discard(1)
# print(conjunto)