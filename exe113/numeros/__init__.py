def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR!!, Digite um numero numeros valido!!\033[m')
            continue
        except(KeyboardInterrupt):
            print("\033[31mInterrupção do sistema\033[m")
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except(ValueError, TypeError):
            print("\033[31mDigite um valor Real corretamente\033[m")
        except(KeyboardInterrupt):
            return 0
        else:
            return n

