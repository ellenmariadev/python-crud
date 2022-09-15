class Arquivo:
    def arquivoExiste(nome):
        try:
            arquivo = open(nome, 'rt')
            arquivo.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def criarArquivo(nome):
        try:
            arquivo = open(nome, 'wt+')
            arquivo.close()
        except:
            print('Erro na criação do arquivo!')
        else:
            print(f'Arquivo {nome} criado com sucesso!')