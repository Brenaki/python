# In[ ]:

import requests as rs

link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

requisicao = rs.get(link)

print(requisicao.json())

# In[ ]:

from flask import Flask

app = Flask(__name__)

@app.route('/') # decorator -> diz em qual link a função vai rodar
def hello_world(): # função
    return {'Ola':'hello', 'mundo':'world!'}

@app.route('/Victor') # decorator -> diz em qual link a função vai rodar
def victor(): # função
    return {'Victor':'Lindo','nome':'Victor'}

@app.route('/mentolira') # decorator -> diz em qual link a função vai rodar
def mentolira(): # função
    return {'Mentolira':'Daora'}

app.run() # coloca o site no ar 

# In[ ]:

from flask import Flask
import pandas as pd

app = Flask(__name__)
tabela = pd.read_excel('Vendas - Dez.xlsx')


@app.route('/') 
def fat():
    faturamento = float(tabela['Valor Final'].sum())
    return {'faturamento': faturamento}

@app.route('/vendas/produtos') 
def vendas_produtos():
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()
    dic_vendas_produtos = tabela_vendas_produtos.to_dict()
    return dic_vendas_produtos

@app.route('/vendas/produtos/<produto>') 
def fat_produto(produto):
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()
    vendas_produto = tabela_vendas_produtos.loc[produto]
    dic_vendas_produto = vendas_produto.to_dict()
    if produto in tabela_vendas_produtos.index:
        return dic_vendas_produto
    else:
        {produto: 'Inexistente'}

app.run() 
