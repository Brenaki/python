#Crie um programa para fazer uma consulta de vendas.
# O usuário do programa deve inserir o nome do programa e,
# caso ele não exista na lista, ele deve ser avisado. Caso exista,
# o programa deve dizer a quantidade de unidades em estoque do produto

# Banco de Dados
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 90, 80]

# Pergunta para o usuário
texto = input('Insira o nome do produto que você está buscando: ')
produto = texto.casefold()

## Verificação se o produto existe:
if produto in produtos:
    # A busca pelo produto indicado
    i = produtos.index(produto)
    qtdeE = estoque[i]
    print('Quantidade do produto {} é de {} unidades.'.format(produto, qtdeE))
else:
    print('{} não existe no estoque!'.format(produto))
    