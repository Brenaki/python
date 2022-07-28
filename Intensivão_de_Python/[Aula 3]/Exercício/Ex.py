from selenium import webdriver as wr
from selenium.webdriver.common.keys import Keys

# 1 - Pegar a cotação do Dolar
## abrir o navegador
navegador = wr.Chrome()

## entrar no google
navegador.get('https://google.com.br/')

## pesquisar cotação dolar no google
# navegador.find_element('como?','codigo dele')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

## pegar a cotação
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

# 2 - Pegar a cotação do Euro
navegador.get('https://google.com.br/')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')

navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

# 3 - Pegar a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')

cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',','.')

print(cotacao_ouro)

# Fechando o navegador

navegador.quit()

# 4 - Atualizar a base de dados
import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')
print(tabela)

# 5 - Recalcular os preços

## Atualizar as cotações
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

## Preço de Compra = Preço Original * Cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

## Preço de Venda = Preço de Compra * Margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

print(tabela)

# 6 - Exportar a base de dados
tabela.to_excel('Produtos Novo.xlsx', index=False)