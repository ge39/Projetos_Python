def leiaInt(msg):
    valido = False
    while not valido:
        entrada = int(input(msg)).strip()
        if entrada.isalpha() or entrada.isfloat():
            print(f'\033[31mValor {entrada} incorreto, Digite um valor do Tipo inteiro\033[m')
        else:
            valido = True
            return int(entrada)
