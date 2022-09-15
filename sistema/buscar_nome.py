# coding: cp1252

import json

arq = 'dados.json'


def buscar_inscrito():
    with open(arq, "r", encoding='utf8') as data_file:
        data = json.load(data_file)

    _nome = str(input('Insira o nome do inscrito: ')).upper()
    finder = False
    for linha in data:
        if linha['NOME'] == _nome:
            finder = True
            print(
                f'\n\033[1mId: {linha["ID"]}\033[m\n\033[1m{linha["NOME"]}\033[m\nCPF: {linha["CPF"]}\nNota: {linha["NOTA"]}\nCurso: {linha["CURSO"]}\nGrau: {linha["GRAU"]}\nTurno: {linha["TURNO"]}\nCota: {linha["COTA"]}\n\n')
            break
    if finder == False:
        print(f'\033[31mInscrito não encontrado!\033[m')
