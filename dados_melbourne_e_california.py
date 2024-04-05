import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#carregar os dados dois arquivos CSV
dados1 = pd.read_csv('C:\\Python\\trabalhopratico\\dados_combinado_california.csv')
dados2 = pd.read_csv('C:\\Python\\trabalhopratico\\dados_combinado_melbourne.csv')

print("Dados do ficheiro 1:")
print(dados1.head())
print("\nDados do ficheiro 2:")
print(dados2.head())

###Integração de Dados
df_combinado = pd.concat([dados1, dados2], axis=0)

print("\nConjunto de dados combinado:")
print(df_combinado.head())

df_combinado.to_csv('dados_combinados.csv', index=False)

dados_combinados = df_combinado.drop(columns={'Population','Households', 'Distance_to_LA', 'Distance_to_SanDiego', 'Distance_to_SanJose', 'Distance_to_SanFrancisco', 'Tot_Rooms', 'Suburb', 'Address', 'Type', 'Method', 'Postcode', 'Bedroom2', 'Car', 'BuildingArea', 'CouncilArea', 'Regionname'})

nome_arquivo = 'dados_combinados.csv'
df = pd.read_csv('C:\\Python\\trabalhopratico\\dados_combinados.csv')

valores_ausentes = df.isnull().sum()

# Cria o gráfico de barras
plt.figure(figsize=(10, 6))
valores_ausentes.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Valores Ausentes por Coluna')
plt.xlabel('Coluna')
plt.ylabel('Quantidade de Valores Ausentes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()