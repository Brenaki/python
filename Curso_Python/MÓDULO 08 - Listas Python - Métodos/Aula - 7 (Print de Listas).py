# 2 Opções:

# print 'normal'
# método join -> texto.join(lista)

produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']
print(produtos)

print('\n'.join(produtos))

# lista = texto.split(separador)

produtos = 'apple tv, mac, iphone x, ipad, apple watch, mac book, airpods'

lista = produtos.split(', ')

print(lista)
print('\n'.join(lista))