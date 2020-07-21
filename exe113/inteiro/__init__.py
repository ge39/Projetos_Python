def leiaInt(msg):
    valido = False
    while not valido:
        entrada = (input(msg))

        if entrada.isfloat():
            print(f'\033[31mValor {entrada} incorreto, Digite um valor do Tipo inteiro\033[m')
            return (entrada)
        else:
            valido = True
            return (entrada)
