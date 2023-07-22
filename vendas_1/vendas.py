import pandas as pd

#importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualização da base de dados
pd.set_option('display.max_columns', None)
#print(tabela_vendas)

# faturamento por loja
#tabela_vendas.groby('ID Loja').sum()

faturação = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

#print(faturação)
# quantidade de produtos por loja
quantidade_produtos = tabela_vendas[['Produto', 'Quantidade']].groupby('Produto').sum()
print(quantidade_produtos)

# ticket médio por produto

#enviar mail

