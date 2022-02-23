def escrever_arquivo(texto):
    diretorio = ('D:/CODE/PYTHON/PROJECT_1/teste.txt')
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append(({aluno:media(lista_notas)}))
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'D:/CODE/PYTHON/')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'D:/CODE/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # media_notas('notas.txt')
    # escrever_arquivo('First Line.\n')
    # aluno = '\nMaxson, 10, 9, 8, 10'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')


# arquivo = open('teste.txt', 'a')
# arquivo.write('\nEscrevi e sair correndo...')
# arquivo.close()

# arquivo = open('teste.txt', 'w')
# arquivo.write('Escrevi e sair correndo...')
# arquivo.close()
