# coding: cp1252

import json

from interface import Interface
from validations.validar import valid_grau, valid_string, valid_turno, valid_cpf

arq = 'dados.json'


def insert_inscritos():
    with open(arq, "r", encoding='utf8') as data_file:
        data = json.load(data_file)

    while True:
        nome = str(input("Nome: ")).strip().upper()
        if valid_string(nome):
            _nome = nome
            break
        else:
            print('\033[31mERRO: Digite um nome válido.\033[m')

    id = len(data)

    while True:
        cpf = str(input('CPF: '))
        if valid_cpf(cpf):
            _cpf = cpf
            break
        else:
            print('\033[31mERRO: Digite um cpf válido (Apenas números).\033[m')

    nota = float(input('Nota: '))

    while True:
        curso = str(input("Curso: ")).strip().upper()
        if valid_string(curso):
            _curso = curso
            break
        else:
            print('\033[31mERRO: Digite um curso válido.\033[m')

    while True:
        grau = str(input('Grau Acadêmico: ')).strip().capitalize()
        if valid_grau(grau):
            _grau = grau
            break
        else:
            print('\033[31mERRO: Digite o grau corretamente: Bacharelado ou Licenciatura.\033[m')

    while True:
        turno = str(input('Turno: ')).strip().capitalize()
        if valid_turno(turno):
            _turno = turno
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

    items = {
        "ID": id + 1,
        "NOME": _nome,
        "CPF": _cpf,
        "NOTA": nota,
        "CURSO": _curso,
        "GRAU": _grau,
        "TURNO": _turno,
        "COTA": cota
    }

    data.append(items)
    with open(arq, 'w') as connect:
        json.dump(data, connect)
    print(f'\033[32mRegistro {nome} adicionado.\033[m')
