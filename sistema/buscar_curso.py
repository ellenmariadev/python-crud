# coding: cp1252

import json

arq = 'dados.json'


def select_curso():
    with open(arq, "r", encoding='utf8') as data_file:
        data = json.load(data_file)

    _curso = str(input('Digite o nome do curso: ')).strip().upper()
    count = 0
    for linha in data:
        if linha['CURSO'] == _curso:
            count = count + 1
            print(
                f'\n\033[1mId: {linha["ID"]}\033[m\n\033[1m{linha["NOME"]}\033[m\nCPF: {linha["CPF"]}\nNota: {linha["NOTA"]}\nCurso: {linha["CURSO"]}\nGrau: {linha["GRAU"]}\nTurno: {linha["TURNO"]}\nCota: {linha["COTA"]}\n\n')
    print(f'\033[1mTotal: {count}\033[m')
