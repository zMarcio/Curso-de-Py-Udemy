import pandas as pd

# # O caminho até o arquivo
caminho = "C:\\Users\\Marcio\\Desktop\\python_Udemy\\Seção 17 Python Pandas Analise e Tratamento de Dados\\arquivos\\Vendas_Jan.xlsx"

# # Configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel(caminho)

print(vendas_DataFrame)
# # Exibe informações sobre quantidade de linhas que tem o DF(DataFrame)
print(vendas_DataFrame.index)

# # columns informações sobre quantidade de colunas que tem o DF(DataFrame)
print(vendas_DataFrame.columns)

# # head exibe por padrão as 5 primeiras linhas
print(vendas_DataFrame.head())

# # head exibe por padrão as 5 primeiras linhas, mas pode exibe a quantidade que vc quiser só colocar entre o parenteses o valor
print(vendas_DataFrame.head(10))

# # tail exibe por padrão as 5 últimas linhas
print(vendas_DataFrame.tail())

# # Para exibir uma coluna específica, coloca-se o nome da coluna em colchetes
print(vendas_DataFrame['Vendedor'])

# # Para exibir uma coluna específica, coloca-se o nome da coluna em colchetes. Assim aparece os 5 primeiros vendedores
print(vendas_DataFrame['Vendedor'].head())

# # Caso eu queria mais de uma coluna posso fazer dessa forma
print(vendas_DataFrame[['Vendedor','Total Vendas']].head())

# # Limitando, colocando um limite inicial e um final de aparição dos dados
print(vendas_DataFrame.loc[5:])

# # Limitando por vendendor
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame['Vendedor'] == 'Leonardo Almeida']
print(vendas_Leonardo_Almeida_DF)

# # Limitando por vendendor e coluna(Total Vendas)
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame['Vendedor'] == 'Leonardo Almeida', ['Vendedor', 'Total Vendas']]
print(vendas_Leonardo_Almeida_DF)

# # Mostra linhas e colunas
print(vendas_DataFrame.shape)

# # Faz a média de venda por vendedor
vendas_DataFrame.groupby('Vendedor')['Total Vendas'].mean()