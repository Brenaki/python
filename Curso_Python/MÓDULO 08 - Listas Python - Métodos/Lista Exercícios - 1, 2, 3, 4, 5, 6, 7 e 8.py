# # Exercícios
# 
# ## 1. Faturamento do Melhor e do Pior Mês do Ano
# 
# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?

# In[]:


# Dados
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# Juntando 2 semestres
vendas = vendas_1sem + vendas_2sem
print(vendas)

# Descobrindo Maior ou Menor valor de vendas
MaiorV = vendas.index(max(vendas))
MenorV = vendas.index(min(vendas))

print(MaiorV)
print(MenorV)

print('\n', vendas[10], vendas[11])


# ## 2. Continuação
# 
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# 
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
# 
# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista

# In[]:


# Melhor e o Pior
print('''
O melhor mês do ano em vendas foi {} com um faturamento de {}.
O pior mês do ano em vendas foi {} com um faturamento de {}.\n
'''.format(meses[10], vendas[10], meses[11], vendas[11]))

# Faturmento Total
fTotal = sum(vendas)
print('Faturamento total do ano foi R$ {:,}'.format(fTotal))

# Percentual
perC = vendas[10] / fTotal
print('O melhor mês representou {:.2%} das vendas do ano todo'.format(perC))


# ## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")
# 
# Dica: o método remove retira um item da lista.

# In[]:


top3 = []


# In[]:


# Top 1
print(vendas)
MaiorV = max(vendas)
top3.append(MaiorV)
vendas.remove(MaiorV)
# Top 2
MaiorV = max(vendas)
top3.append(MaiorV)
vendas.remove(MaiorV)
# Top 3
MaiorV = max(vendas)
top3.append(MaiorV)
print(top3)
vendas.remove(MaiorV)
print(vendas)

