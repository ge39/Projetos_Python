'''
    Crie um pacote chamado utilidadesCev wue tenha dois mod110 internos
    chamado moeda e dado.

    Transfira todos as funções utilizadas nos desafios 107, 108 e 109 para
    o primeiro pacote e mantenha tudo funcionando.

'''
from exe111.utilidadescev import moeda

numero = float(input("Digite o Preço: R$ "))
moeda.resumo(numero, 10, 30)