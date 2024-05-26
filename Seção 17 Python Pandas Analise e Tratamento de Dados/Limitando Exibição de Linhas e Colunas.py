import pandas as pd

# # O caminho até o arquivo
caminho = "C:\\Users\\Marcio\\Desktop\\python_Udemy\\Seção 17 Python Pandas Analise e Tratamento de Dados\\arquivos\\Vendas_Jan.xlsx"

# # Configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel(caminho)

print(vendas_DataFrame)
# # Exibe informações sobre quantidade de linhas que tem o DF(DataFrame)
print(vendas_DataFrame.index)
