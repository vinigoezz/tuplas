'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
produtospreços = ('Lápis', 1.75,
                  'Borracha', 2,
                  'Caderno', 15.90,
                   'Mochila', 30,
                   'Tesoura', 5, 
                   'Livro', 12)
for pos in range(0, len(produtospreços)):
    if pos % 2 ==0:
     print(f'{produtospreços[pos]:-<30}', end='')
    else:
       print(f'R${produtospreços[pos]:>5}')
