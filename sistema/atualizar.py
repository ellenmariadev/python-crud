# coding: cp1252

import json

from interface import Interface
from validations.validar import valid_grau, valid_string, valid_turno, valid_cpf

arq = 'dados.json'


def update_inscritos():
    with open(arq, "r", encoding='utf8') as data_file:
        data = json.load(data_file)

    _id = int(input("Insira o ID do inscrito: "))

    while True:
        nome = str(input("Nome: ")).strip().upper()
        if valid_string(nome):
            new_nome = nome
            break
        else:
            print('\033[31mERRO: Digite um nome válido.\033[m')

    while True:
        cpf = str(input('CPF: '))
        if valid_cpf(cpf):
            new_cpf = cpf
            break
        else:
            print('\033[31mERRO: Digite um cpf válido (Apenas números).\033[m')

    new_nota = float(input('Nota: '))

    while True:
        curso = str(input("Curso: ")).strip().upper()
        if valid_string(curso):
            new_curso = curso
            break
        else:
            print('\033[31mERRO: Digite um curso válido.\033[m')

    while True:
        grau = str(input('Grau Acadêmico: ')).strip().capitalize()
        if valid_grau(grau):
            new_grau = grau
            break
        else:
            print('\033[31mERRO: Digite o grau corretamente: Bacharelado ou Licenciatura.\033[m')

    while True:
        turno = str(input('Turno: ')).strip().capitalize()
        if valid_turno(turno):
            new_turno = turno
            break
        else:
            print('\033[31mERRO: Digite o turno: Matutino, Vespertino, Noturno ou Integral.\033[m')

    while True:
        opc1 = 'Ampla Concorrência'
        opc2 = 'Candidato (s) que tenham cursado todo o Ensino Médio e os últimos quatro anos do Ensino Fundamental em Escola Pública e que se autodeclararam negros.'
        opc3 = 'Candidato (s) que tenham cursado todo o Ensino Médio e os últimos quatro anos do Ensino Fundamental em Escola Pública e que sejam índios reconhecidos pela FUNAI ou moradores de comunidades remanescentes de quilombos registrados na Fundação Cultural Palmares.'
        cotas = Interface.cotas([opc1, opc2, opc3])
        if cotas == 1:
            cota = opc1
            break
        elif cotas == 2:
            cota = opc2
            break
        elif cotas == 3:
            cota = opc3
            break
        else:
            print('\033[31mERRO: Digite uma opção válida.\033[m')

    for inscrito in data:
        if inscrito["ID"] == _id:
            inscrito["NOME"] = new_nome
            inscrito["CPF"] = new_cpf
            inscrito["NOTA"] = new_nota
            inscrito["CURSO"] = new_curso
            inscrito["GRAU"] = new_grau
            inscrito["TURNO"] = new_turno
            inscrito["COTA"] = cota

    with open(arq, "w") as connect:
        json.dump(data, connect)
        print(f'\033[32mInscrito atualizado!\033[m')