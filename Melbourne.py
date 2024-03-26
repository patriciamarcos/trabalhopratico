import pandas as pd
###1. Reclha de Dados
#carregar os dados dois arquivos CSV
dados1 = pd.read_csv('arquivo1.csv')
dados2 = pd.read_csv('arquivo.csv')

#Exibie as rimeiras linhas para garantir que os dados foram carregados
print(f"Dados do arquivo 1:")
print(dados1.head())

print(f"Dados do arquivo 2:")
print(dados2.head())

###2. Integração de Dados
#combinar os dois conjuntos de dados em um único conjunto de dados
conjunto_de_dados = pd.concat([dados1, dados2], ignore_index=True)

#exigibir as primeiras linhas do conjunto de dados ombinado
print(f"conjunto de dados combinado:")
print(conjunto_de_dados.head())