def linha(tam = 42):
    return '\033[0;34m-\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[0;36mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())