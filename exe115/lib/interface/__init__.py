def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[m31Usuaário preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '\033[35m-\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[34mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[m - {item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[34mSua opção:\033[m ')
    return opc