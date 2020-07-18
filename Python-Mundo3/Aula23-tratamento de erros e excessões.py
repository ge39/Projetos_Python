'''
    TRATAMENTO DE ERROS E EXCEÇÕES.

'''
def ln():
    print('*' * 50)

#programa principal
ln()
'''
try
    operacao
Exception
    error
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador :'))
    r = a / b
#except Exception as erro:
except (ValueError, TypeError):
    print(f'Tivemos um problema com os dados que voce digitou :')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! muito obrigado.')
