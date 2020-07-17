def aumentar(preco = 0, taxa = 0,formato = False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
   res= preco * 2
   return res if not formato else moeda(res)


def metade(preco = 0, formato = False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0 ,moeda = 'R$', formato = False):

 return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, taxaA=10, taxaR=5):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do preço   \t{dobro(preco, True)}')
    print(f'Metade do preço  \t{metade(preco, True)}')
    print(f'Com {taxaA}% do preço: \t{aumentar(preco,taxaA, True)}')
    print(f'Com {taxaR}% do preço   \t{diminuir(preco, taxaR, True)}')
    print('-' *30)



