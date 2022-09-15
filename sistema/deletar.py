# coding: cp1252

import json

arq = 'dados.json'


def delete_inscrito():
    with open(arq, "r", encoding='utf8') as data_file:
        data = json.load(data_file)

    _id = int(input("Insira o ID do inscrito: "))
    finder = False
    for inscrito in data:
        if inscrito["ID"] == _id:
            data.pop(data.index(inscrito))
            finder = True
            print(f"\033[32mInscrito removido!\033[m")
            break
    with open(arq, "w") as connect:
        json.dump(data, connect)
    if finder == False:
        print(f'\033[31mInscrito inválido!\033[m')
