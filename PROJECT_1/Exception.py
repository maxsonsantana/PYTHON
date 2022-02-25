lista = [1, 10, 7]
arquivo = open('notas.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[2]
    x = divisao
    print('fechando arquivo')
    arquivo.close()
# except Exception as ex:
#     print('Erro desconhecido - Erro: {}'.format(ex))
# except BaseException as ex:
#     print('Erro desconhecido - Erro: {}'.format(ex))
except ZeroDivisionError:
    print('Não dar pra dividir por 0')
except IndexError:
    print('Erro ao acessar índice inválido')
else:
    print('Código executado sem erros!')
finally:
    print('Sempre Executa')
    print('Fechando o arquivo')
    arquivo.close()