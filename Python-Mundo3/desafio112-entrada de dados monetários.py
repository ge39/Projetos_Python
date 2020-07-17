'''
    Dentro do pacote utilidadeCev que criamos no desafio 111,
    temos um módulo chamado dado. Crie uma função leiaDinheiro()
    que seja caoaz de funcionar como a função input().
    mas com uma validação de dados para aceitar apenas valores que sejam monetários.
'''
from exe112.utilidadescev import moeda, dado

numero = dado.leiaDinheiro(("Digite o Preço: R$ "))
moeda.resumo(numero, 10, 30)