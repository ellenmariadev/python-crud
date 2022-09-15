class Interface:

    def leiaInt(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('\033[31mERRO: Digite uma opção válida.\033[m')
                continue
            except(KeyboardInterrupt):
                print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
                return 0
            else:
                return n

    def linha(tam=14):
        return '-=-' * tam

    def cabecalho(txt):
        print(Interface.linha())
        print(txt.center(42))
        print(Interface.linha())

    def menu(lista):
        Interface.cabecalho('CHAMADA REGULAR 2021 - UESC')
        for index, item in enumerate(lista, 1):
            print(f'\033[33m{index}\033[m - \033[34m{item}\033[m')
        print(Interface.linha())
        opc = Interface.leiaInt('> Sua Opção: ')
        return opc

    def cotas(lista):
        print('Modalidade de Concorrência:\n')
        for index, item in enumerate(lista, 1):
            print(f'\033[33m{index}\033[m - \033[34m{item}\033[m')
        opc = Interface.leiaInt('> Sua Opção: ')
        return opc