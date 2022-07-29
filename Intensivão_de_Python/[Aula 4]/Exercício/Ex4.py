# In[ ]:

# 1 - Entendimento do Desafio
# 2 - Entendimento da Área/Empresa
# 3 - Extração/Obtenção de Dados

import pandas as pd

tabela = pd.read_csv(r'.\advertising.csv')

print(tabela)


# In[ ]:


# 4 - Ajuste de Dados(Tratamento/Limpeza)
# 5 - Análise Exploratória
import seaborn as sns
import matplotlib.pyplot as plt

## Criar o grafico
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)

## Exibir o grafico
plt.show()


# In[ ]:


# 6 - Modelagem + Algoritmos(A.I, se necessário)

## y - quem você quer prever (Vendas)
## x - é o resto todo (quem voCê vai usar pra fazer a previsão)

x = tabela[['TV', 'Radio', 'Jornal']]
y = tabela['Vendas']

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)


# In[ ]:


from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

## Cria a A.I
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

## Treina a A.I
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


# In[ ]:


## Fazer previsor nos testes

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

## Comparar a melhor resposta

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))


# In[ ]:


# 7 - Interpretção de Resultados

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['arvore decisao'] = previsao_arvoredecisao
tabela_auxiliar['regresso linear'] = previsao_regressaolinear

plt.figure(figsize=(18,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()


# In[ ]:


## Como fazer uma nova previsão?
### o melhor modelo é a árvore de decisão

novos = pd.read_csv(r'.\novos.csv')
print(novos)


# In[ ]:

print(modelo_arvoredecisao.predict(novos))