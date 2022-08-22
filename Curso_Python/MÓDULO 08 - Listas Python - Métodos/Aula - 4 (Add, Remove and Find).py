#Crie um programa para remove e adicionar produtos da Apple.
# Caso ele for remover, verificar se existe o produto na lista, se existir
# excutar normal, se não mostrar mensagem de erro.

# Produtos
produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']

# Adicionar ou Remover?
escolha = input('Você deseja adicionar(1) ou remover(2) ou pesquisar(3) produtos: ')

## Só por a caso
### Adicionando produto
if escolha == '1':
    texto = input('Insira nome do produto: ')
    produto = texto.casefold()
    produtos.append(produto)
    print('O produto {} foi adicionando a lista!'.format(produto))
    print(produtos)
### Removendo produto
elif escolha == '2':
    texto = input('Insira nome do produto: ')
    produto = texto.casefold()
    # Só mais uma verificação!
    try:
        produtos.remove(produto)
        print('Produto {} removido com sucesso!'.format(produto))
        print(produtos)
    except:
        print('Erro!')
elif escolha == '3':
    print(produtos)
### O que você escreveu?
else:
    print('Erro!')
    