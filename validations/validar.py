# coding: cp1252
import re

# STRING
string = re.compile(r"^[a-zA-Z]")


def valid_string(s):
    return string.match(s)


# CPF
cpf = re.compile("^[0-9]{11}")


def valid_cpf(c):
    return cpf.match(c)


# GRAU
def valid_grau(g):
    if g == 'Bacharelado' or g == 'Licenciatura':
        return True
    else:
        return False


def valid_turno(t):
    if t == 'Noturno' or t == 'Integral' or t == 'Matutino' or t == 'Vespertino':
        return True
    else:
        return False
