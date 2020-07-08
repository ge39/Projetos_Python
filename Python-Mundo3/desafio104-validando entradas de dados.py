''''
    Crie um programa que tenha a função leiaInt(),que vai funcionar de forma semelhante input() do python.
    só que fazendo validações para aceitar apenas um valor numerico.
    EX:
    n = leiant('digite um numero')

'''
def leiaInt(msg):
    ok = False  #variavel recebe o valor false
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric(): #se o numero digitado for um numero
            valor = int(n)  #a variavel valor recebe o valor de n
            ok = True       #variavel "N" recebe o valor true
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:  # se a variavel "OK" mudou seu valor para True, finalize
            print('ok, ',end='')
            break
    return valor


#programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce imprimiu o numero {n}')

