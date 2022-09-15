# coding: cp1252

from time import sleep
import pandas as pd
from arquivo import Arquivo
from interface import Interface

from sistema.adicionar import insert_inscritos
from sistema.atualizar import update_inscritos
from sistema.buscar_nome import buscar_inscrito
from sistema.deletar import delete_inscrito
from sistema.buscar_curso import select_curso

arq = 'dados.json'

if not Arquivo.arquivoExiste(arq):
    Arquivo.criarArquivo(arq)
    csv_file = pd.DataFrame(pd.read_csv("listaregular.csv", sep = ";", header = 0, index_col = False, encoding='latin-1'))
    csv_file.to_json("dados.json", orient = "records", default_handler = None, force_ascii=False)

titulo = "Universidade Estadual de Santa Cruz"
subtitulo = "Campus Ilhéus (Salobrinho)"
print(f'\033[1m\n{titulo.center(42)}\n{subtitulo.center(40)}\n\033[m')

while True:
    user_option = Interface.menu(['Cadastrar', 'Buscar Curso', 'Buscar Inscrito', 'Editar', 'Remover', '[Sair]'])
    if user_option == 1:
        Interface.cabecalho('CADASTRAR')
        insert_inscritos()
    elif user_option == 2:
        Interface.cabecalho('BUSCAR')
        select_curso()
    elif user_option == 3:
        Interface.cabecalho('BUSCAR')
        buscar_inscrito()
    elif user_option == 4:
        Interface.cabecalho('ATUALIZAR')
        update_inscritos()
    elif user_option == 5:
        Interface.cabecalho('REMOVER')
        delete_inscrito()
    elif user_option == 6:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(2)