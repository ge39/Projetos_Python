'''
    Modularização
    1 - surgiu no inicio dos anos 60: , para resolver problemas
    2 - Sistemas ficando cada vez maior:
        o foco principal é dividir um programa grande com muitas funcionalidades
    em pequenos programas
    3 - aumentar a legibilidade: divide em modulos com determinado assunto
    4 - Facilitar a Manutenção: pegar um problemao e dividir em pequenos problemas

    VANTAGENS:
    1 - Organização do codigo
    2 - facilidade na manutenção
    3 - Ocultação de codigo detalhado
    4 - Reutilização do codigo em putros projetos
'''

def ln():
    print('*' *100)

def fatorial(n):
    f = 1
    for c in range(1, n + 1):
         f*=c
    return f


#programa principal
ln()
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O Fatorial de {num} é {fat}")
ln()